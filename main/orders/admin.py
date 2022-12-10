from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Order




class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email',
                    'address', 'postal_code', 'city', 'paid',
                    'created', 'updated', 'status']
    list_filter = ['paid', 'created', 'updated','status']
    model = Order


admin.site.register(Order, OrderAdmin)
