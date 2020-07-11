from django.contrib import admin
from .models import Visit


class VisitAdmin(admin.ModelAdmin):
    fields = ('start_at' , 'end_at', 'description' ,'created_at', 'updated_at','purpose')
    list_display = ('start_at' , 'end_at', 'description' ,'created_at', 'updated_at','purpose')


admin.site.register(Visit, VisitAdmin)
