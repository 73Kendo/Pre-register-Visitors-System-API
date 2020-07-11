from django.contrib import admin
from django.urls import path , include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('guests/', include('apps.guests.urls')),
    path('companies/', include('apps.companies.urls')),
    path('sites/', include('apps.sites.urls')),
    path('purposes/', include('apps.purposes.urls')),
    path('visits/', include('apps.visits.urls')),
]
