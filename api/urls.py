from django.urls import path
from rest_framework import routers
from .views import UserAPIView, PetViewSet

router = routers.SimpleRouter()
router.register(r'pets', PetViewSet)

urlpatterns = [
    path('users', UserAPIView.as_view()),
]

urlpatterns += router.urls