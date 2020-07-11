from django.contrib import admin
from .models import Purpose


class PurposeAdmin(admin.ModelAdmin):
    fields = ('name', 'description',)
    list_display = ('name', 'description', 'created_at', 'updated_at',)


admin.site.register(Purpose, PurposeAdmin)
