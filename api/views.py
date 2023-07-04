from rest_framework import viewsets, generics
from django.contrib.auth.models import User
from django_filters.rest_framework import DjangoFilterBackend
from .models import Pet
from .serializers import UserSerializer, PetSerializer
from .filters import IsOwnerFilterBackend


class UserAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PetViewSet(viewsets.ModelViewSet):
    queryset = Pet.objects.select_related('owner')
    serializer_class = PetSerializer
    filter_backends = [IsOwnerFilterBackend, DjangoFilterBackend]
    filterset_fields = ['breed']

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)