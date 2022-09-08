from django.contrib.gis import admin
from .models import WorldBorder


class WorldBorderAdmin(admin.GISModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]


admin.site.register(WorldBorder, WorldBorderAdmin)
