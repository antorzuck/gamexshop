from django.contrib import admin
from base.models import *


admin.site.register(Banner)
class ItemPackageInline(admin.StackedInline):
    model = ItemPackage
    extra = 1


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    inlines = [ItemPackageInline]


@admin.register(ItemPackage)
class ItemPackageAdmin(admin.ModelAdmin):
    list_display = ('name', 'item', 'created_at')
    list_filter = ('item',)

admin.site.register(Category)
admin.site.register(Profile)