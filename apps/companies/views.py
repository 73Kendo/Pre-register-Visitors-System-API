from rest_framework import serializers , viewsets
from .models import Company


class  CompanySerializer(serializers.HyperlinkedModelSerializer):
     class Meta:
        model = Company
        fields = ['name' , 'description' ,'created_at', 'updated_at',]

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer