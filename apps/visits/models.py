from django.db import models
from apps.purposes.models import Purpose
from apps.companies.models import Company
from apps.sites.models import Site
from apps.guests.models import Guest

class Visit(models.Model):    
    start_at = models.DateTimeField()
    end_at = models.DateTimeField()
    purpose = models.ForeignKey(Purpose, on_delete=models.PROTECT)  
    company = models.ForeignKey(Company, on_delete=models.PROTECT)
    site = models.ForeignKey(Site, on_delete=models.PROTECT)
    description = models.TextField()
    guest = models.ManyToManyField(Guest,related_name="guests_vist") 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

