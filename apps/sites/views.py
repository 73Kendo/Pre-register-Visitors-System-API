from rest_framework import serializers , viewsets
from .models import Site


class  SiteSerializer(serializers.HyperlinkedModelSerializer):
     class Meta:
        model = Site
        fields = ['name' , 'description' ,'created_at', 'updated_at',]

class SiteViewSet(viewsets.ModelViewSet):
    queryset = Site.objects.all()
    serializer_class = SiteSerializer