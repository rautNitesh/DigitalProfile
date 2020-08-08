from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views.citizen_views import CitizenViewSet


# router = DefaultRouter()
# router.register('citizen', CitizenViewSet)

urlpatterns = [
    # path('', include(router.urls)),
    path('', CitizenViewSet.as_view(), name="citizen_list")
]
