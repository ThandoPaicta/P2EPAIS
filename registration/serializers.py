# registration/serializers.py
from rest_framework import serializers
from registration.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
