"""Collector Admin model definition"""

from typing import Optional
from django.contrib import admin
from django.contrib.auth.models import Group
from django.db.models import QuerySet
from django.http import HttpRequest
from django.utils import timezone
from collector.models import CollectorData, ExpiringSoonCollectorData
from collector.utils.date_utils import days_from_now
from django.http import HttpResponse
from datetime import datetime
from rangefilter.filters import DateRangeFilterBuilder
import csv

admin.site.unregister(Group)


class ExpiringSoonCollectorDataAdmin(admin.ModelAdmin):
    """Admin class for managing the display of `ExpiringSoonCollectorData` model.

    This admin view is configured to be read-only and displays a list of collectors
    whose subscription is expiring soon (within a specified timeframe).
    """

    readonly_fields = ("created_at", "last_modified")
    list_display = (
        "created_at",
        "last_modified",
        "first_name",
        "last_name",
        "expiration_date",
        "status",
    )

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


class CollectorDataAdmin(admin.ModelAdmin):
    search_fields = ["first_name", "last_name"]
    list_filter = (("expiration_date", DateRangeFilterBuilder()),)

    def export_as_csv(
        self, request: HttpRequest, queryset: QuerySet["CollectorData"]
    ) -> HttpResponse:
        """
        Export selected CollectorData objects as a CSV file.

        Args:
            request: The HTTP request object.
            queryset: The queryset of selected CollectorData instances.

        Returns:
            HttpResponse: A response containing the CSV data.
        """
        current_timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"collector_data_{current_timestamp}.csv"
        response = HttpResponse(content_type="text/csv")
        response["Content-Disposition"] = f"attachment; filename={filename}"

        writer = csv.writer(response)

        writer.writerow(
            [
                "First Name",
                "Last Name",
                "Status",
                "Email",
                "Phone Number",
                "Birth Date",
                "Place of Birth",
                "Place of Residence",
                "Postal Code",
                "Personal Number",
                "Entry Date",
                "Expiration Date",
                "Reminder Count",
                "Note",
                "Created At",
            ]
        )

        for obj in queryset:
            writer.writerow(
                [
                    obj.first_name,
                    obj.last_name,
                    obj.status,
                    obj.email,
                    obj.phone_number,
                    obj.birth_date,
                    obj.place_of_birth,
                    obj.place_of_residence,
                    obj.postal_code,
                    obj.personal_number,
                    obj.entry_date,
                    obj.expiration_date,
                    obj.reminder_count,
                    obj.note,
                    obj.created_at,
                ]
            )

        return response

    actions = ["export_as_csv"]


admin.site.register(CollectorData, CollectorDataAdmin)
admin.site.register(ExpiringSoonCollectorData, ExpiringSoonCollectorDataAdmin)
