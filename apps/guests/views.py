from rest_framework import serializers , viewsets
from .models import Guest


class  GuestSerializer(serializers.HyperlinkedModelSerializer):
     class Meta:
        model = Guest
        fields = ['first_name', 'last_name', 'pesel' , 'name',
                  'created_at', 'updated_at',
                  ]

class GuestViewSet(viewsets.ModelViewSet):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer
