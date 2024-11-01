from django.contrib import admin
from collector.models import CollectorData
from django.contrib.auth.models import Group

admin.site.register(CollectorData)
admin.site.unregister(Group)
