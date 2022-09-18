from django.contrib import admin
from .models import File
# Register your models here.

class FileAdmin(admin.ModelAdmin):
    list_display = ["id", "open", "high", "low","close", "date"]
admin.site.register(File, FileAdmin)