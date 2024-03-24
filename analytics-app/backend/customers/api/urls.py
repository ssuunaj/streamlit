from rest_framework import routers
from .views import CustomerViewSet

customer_router = routers.DefaultRouter()

customer_router.register(r'customers', CustomerViewSet)