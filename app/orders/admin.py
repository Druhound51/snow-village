# coding=utf-8
from django.contrib import admin
from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    # readonly_fields = ['product']
    can_delete = False

    def get_readonly_fields(self, request, obj=None):
        result = list(set(
            [field.name for field in self.opts.local_fields]
        ))
        result.remove('id')
        return result


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'gender', 'email', 'created']
    list_display_links = ['id', 'name']
    readonly_fields = ['created', 'name', 'gender', 'email', 'phone']
    list_filter = ['created']
    inlines = [OrderItemInline]

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(Order, OrderAdmin)
