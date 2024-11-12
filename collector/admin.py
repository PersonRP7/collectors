"""Collector Admin model"""

from typing import Optional
from django.contrib import admin
from django.contrib.auth.models import Group
from django.db.models import QuerySet
from django.http import HttpRequest
from django.utils import timezone
from collector.models import CollectorData, ExpiringSoonCollectorData
from collector.utils.date_utils import days_from_now

admin.site.unregister(Group)


class ExpiringSoonCollectorDataAdmin(admin.ModelAdmin):
    """Admin class for managing the display of `ExpiringSoonCollectorData` model.

    This admin view is configured to be read-only and displays a list of collectors
    whose subscription is expiring soon (within a specified timeframe).
    """

    list_display = ("first_name", "last_name", "expiration_date", "status")

    def get_queryset(self, request: HttpRequest) -> QuerySet["CollectorData"]:
        """Get the queryset for collectors expiring within 14 days but not yet expired.

        Args:
            request (HttpRequest): The HTTP request object.

        Returns:
            QuerySet[CollectorData]: A filtered queryset of collectors expiring soon.
        """
        queryset = super().get_queryset(request)
        today = timezone.now().date()
        return queryset.filter(
            expiration_date__lte=days_from_now(14), expiration_date__gte=today
        )

    def has_add_permission(self, request: HttpRequest) -> bool:
        """Disable the add permission for this admin view."""
        return False

    def has_change_permission(
        self, request: HttpRequest, obj: Optional[CollectorData] = None
    ) -> bool:
        """Disable the change permission for this admin view."""
        return False

    def has_delete_permission(
        self, request: HttpRequest, obj: Optional[CollectorData] = None
    ) -> bool:
        """Disable the delete permission for this admin view."""
        return False

    def has_view_permission(
        self, request: HttpRequest, obj: Optional[CollectorData] = None
    ) -> bool:
        """Enable the view permission for this admin view."""
        return True


admin.site.register(CollectorData)
admin.site.register(ExpiringSoonCollectorData, ExpiringSoonCollectorDataAdmin)
