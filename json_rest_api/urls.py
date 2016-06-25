from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'provider', views.ProviderViewSet)
router.register(r'service_area', views.ServiceAreaViewSet)

urlpatterns = []
urlpatterns += router.urls
