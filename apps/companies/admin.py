from django.contrib import admin
from .models import Company


class CompanyAdmin(admin.ModelAdmin):
    fields = ('name', 'description',)
    list_display = ('name', 'description', 'created_at', 'updated_at',)


admin.site.register(Company, CompanyAdmin)
