from rest_framework import serializers , viewsets
from .models import Purpose


class  PurposeSerializer(serializers.HyperlinkedModelSerializer):
     class Meta:
        model = Purpose
        fields = ['name' , 'description' ,'created_at', 'updated_at',]

class PurposeViewSet(viewsets.ModelViewSet):
    queryset = Purpose.objects.all()
    serializer_class = PurposeSerializer