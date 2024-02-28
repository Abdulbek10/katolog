from django.contrib import admin
from .models import Kinokatalog

@admin.register(Kinokatalog)
class KinokatalogAdmin(admin.ModelAdmin):
    list_display = ["name","adress","phone","email"]
    list_filter = ["name","adress"]