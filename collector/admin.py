from django.contrib import admin
from collector.models import CollectorData, ExpiringSoonCollectorData
from django.contrib.auth.models import Group
from collector.utils.date_utils import days_from_now

admin.site.unregister(Group)


class ExpiringSoonCollectorDataAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "expiration_date", "status")

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.filter(expiration_date__lte=days_from_now(14))

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_view_permission(self, request, obj=None):
        return True


admin.site.register(CollectorData)
admin.site.register(ExpiringSoonCollectorData, ExpiringSoonCollectorDataAdmin)
