from django.contrib import admin

from . import models, forms


class UserAdmin(admin.ModelAdmin):
    form = forms.UserChangeForm
    add_form = forms.UserCreationForm

    def get_form(self, request, obj=None, **kwargs):
        if obj is None:
            return self.add_form
        return super().get_form(request, obj, **kwargs)

    list_display = ["username", "first_name", "last_name", "role"]


admin.site.register(models.User, UserAdmin)
admin.site.register(models.Restaurant)
admin.site.register(models.RestaurantItem)
admin.site.register(models.Cart)
admin.site.register(models.CartItem)
admin.site.register(models.Order)
