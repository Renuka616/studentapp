# for Viewset
from .viewsets import CustomerViewSet
from rest_framework.routers import DefaultRouter

# View set routers

routers = DefaultRouter()
routers.register(r'api/customerviewset/',CustomerViewSet,basename='customer')
urlpatterns = routers.urls