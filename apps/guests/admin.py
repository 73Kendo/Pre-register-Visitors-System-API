from django.contrib import admin
from .models import Guest


class GuestAdmin(admin.ModelAdmin):
    fields = ('first_name', 'last_name', 'pesel' , 'name',)
    list_display = ('first_name', 'last_name', 'pesel' , 'name', 'created_at', 'updated_at',)


admin.site.register(Guest, GuestAdmin)