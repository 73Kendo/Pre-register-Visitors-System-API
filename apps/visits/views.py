from rest_framework import serializers , viewsets
from .models import Visit
from apps.purposes.models import Purpose


class  VisitSerializer(serializers.HyperlinkedModelSerializer):
  
    
    class Meta:
        model = Visit
        fields = ['start_at' , 'end_at', 'description' ,'created_at', 'updated_at','purpose','company','site','guest',]

class VisitViewSet(viewsets.ModelViewSet):
    queryset = Visit.objects.all()
    serializer_class = VisitSerializer

        