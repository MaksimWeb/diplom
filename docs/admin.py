from django.contrib import admin
from .models import SomeModel
from simple_history.admin import SimpleHistoryAdmin

# Register your models here.
admin.site.register(SomeModel, SimpleHistoryAdmin)
