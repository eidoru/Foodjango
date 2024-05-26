from django.db import models
from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class UserManager(BaseUserManager):
    def create_user(self, username, password=None, first_name="", last_name="", role=""):
        if username is None:
            raise TypeError("Users must have a username.")
        user = self.model(username=username,
                          first_name=first_name, last_name=last_name, role=role)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, password=None, first_name="", last_name=""):
        if password is None:
            raise TypeError("Superusers must have a password.")
        user = self.create_user(username, password, first_name, last_name)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):
    RUNNER = "runner"
    PATRON = "patron"
    VENDOR = "vendor"
    ROLE_CHOICES = {
        RUNNER: "runner",
        PATRON: "patron",
        VENDOR: "Vendor",
    }
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    first_name = models.CharField(
        max_length=255, blank=True)
    last_name = models.CharField(
        max_length=255, blank=True)
    role = models.CharField(
        max_length=255, choices=ROLE_CHOICES, default="patron")
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    USERNAME_FIELD = "username"
    PASSWORD_FIELD = "password"
    REQUIRED_FIELDS = ["first_name", "last_name"]
    objects = UserManager()


class Restaurant(models.Model):
    name = models.CharField(max_length=255, unique=True)
    vendor = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="vendor")


class RestaurantItem(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.00)
    restaurant = models.ForeignKey(
        Restaurant, on_delete=models.CASCADE, related_name="restaurant_item")


class Cart(models.Model):
    total_price = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.00)
    patron = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="patron")
    restaurant = models.OneToOneField(
        Restaurant, on_delete=models.CASCADE, related_name="restaurant")


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    restaurant_item = models.OneToOneField(
        RestaurantItem, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)


class Order(models.Model):
    STATUS_PENDING = "pending"
    STATUS_IN_PROGRESS = "in_progress"
    STATUS_COMPLETE = "complete"
    STATUS_CHOICES = [
        (STATUS_PENDING, "Pending"),
        (STATUS_IN_PROGRESS, "In Progress"),
        (STATUS_COMPLETE, "Complete"),
    ]
    cart = models.OneToOneField(Cart, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=100, choices=STATUS_CHOICES, default=STATUS_PENDING)
    runner = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="runner")


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    restaurant_item = models.OneToOneField(
        RestaurantItem, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.00)
