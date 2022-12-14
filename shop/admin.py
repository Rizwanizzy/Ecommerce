from django.contrib import admin
from .models import *


# Register your models here.
class categadmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('id', 'name')


admin.site.register(categ, categadmin)


class productadmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name', 'category', 'stock', 'price', 'availability')
    list_editable = ['stock', 'price', 'availability']


admin.site.register(product, productadmin)
