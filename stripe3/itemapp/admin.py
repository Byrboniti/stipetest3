from django.contrib import admin
from .models import Item,Price
# Register your models here.



class PriceInlineAdmin(admin.TabularInline):
    model = Price
    extra = 0


class ItemAdmin(admin.ModelAdmin):
    inlines = [PriceInlineAdmin]


admin.site.register(Item, ItemAdmin)