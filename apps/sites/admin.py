from django.contrib import admin
from .models import Site


class SiteAdmin(admin.ModelAdmin):
    fields = ('name', 'description',)
    list_display = ('name', 'description', 'created_at', 'updated_at',)


admin.site.register(Site, SiteAdmin)
