from rest_framework import serializers
from .models import ALBUM

class ALBUMSerializer(serializers.ModelSerializer):
    class Meta:
        model = ALBUM
        # field = ('id', 'mobile', 'fullname')
        fields = '__all__'