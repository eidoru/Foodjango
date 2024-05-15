from django.contrib import admin
from . import models


admin.site.register(models.User)
admin.site.register(models.Restaurant)
admin.site.register(models.MenuItem)
admin.site.register(models.Cart)
admin.site.register(models.CartItem)
admin.site.register(models.Order)
