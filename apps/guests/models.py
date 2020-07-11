from django.db import models

class Guest(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=60)
    name = models.CharField(max_length=50)
    pesel = models.CharField(max_length=11)
    #id_site = models.IntegerField() relacja do innetabeli
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return "{} {}".format(self.first_name,self.last_name)
    
