from django.urls import path
from rest_framework import routers
from .views import UserAPIView, PetViewSet
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

router = routers.SimpleRouter()
router.register(r'pets', PetViewSet)

urlpatterns = [
    path('users', UserAPIView.as_view()),
    path('schema', SpectacularAPIView.as_view(), name='schema'),  # download schema.yaml
    path('schema/swagger', SpectacularSwaggerView.as_view(url_name='schema'))
]

urlpatterns += router.urls
