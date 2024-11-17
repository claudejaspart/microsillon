from rest_framework import serializers
from .models import USER

class USERSerializer(serializers.ModelSerializer):
    class Meta:
        model = USER
        # field = ('id', 'mobile', 'fullname')
        fields = '__all__'