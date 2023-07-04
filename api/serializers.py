from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Pet


class UserSerializer(serializers.ModelSerializer):
    pets = serializers.SlugRelatedField(many=True, read_only=True, slug_field='nickname')

    class Meta:
        model = User
        fields = ['id', 'username', 'pets']


class PetSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Pet
        fields = '__all__'

