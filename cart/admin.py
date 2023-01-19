from django.contrib import admin
from .models import cartlist,items,del_details,orders,ordered_items
# Register your models here.

admin.site.register(cartlist)
admin.site.register(items)
admin.site.register(del_details)
admin.site.register(orders)
admin.site.register(ordered_items)