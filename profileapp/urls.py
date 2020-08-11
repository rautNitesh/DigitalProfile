from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views.citizen_views import CitizenView, ReligionCountView, GenderCount


# router = DefaultRouter()
# router.register('citizen', CitizenViewSet)

urlpatterns = [
    # path('', include(router.urls)),
    path('', CitizenView.as_view(), name="citizen_list"),
    path('religion/', ReligionCountView.as_view(), name='religion_count'),
    path('gender/', GenderCount.as_view(), name='gender_count'),
]
