from django.contrib import admin
from .models import TestDocs
from simple_history.admin import SimpleHistoryAdmin

# Register your models here.
admin.site.register(TestDocs, SimpleHistoryAdmin)
