from django.contrib import admin
from base.models import *


admin.site.register(Banner)
class ItemPackageInline(admin.StackedInline):
    model = ItemPackage
    extra = 1


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'created_at', 'updated_at')
    inlines = [ItemPackageInline]


@admin.register(ItemPackage)
class ItemPackageAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'item', 'created_at', 'updated_at')
    list_filter = ('item',)
