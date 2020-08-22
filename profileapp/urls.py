from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views.citizen_views import (CitizenView, ReligionCountView, GenderCount,
                                  WardGenderCount, CitizenSearchView, WardReligionCount, LiteracyCount, WardLiteracyCount)


# router = DefaultRouter()
# router.register('citizen', CitizenViewSet)

urlpatterns = [
    # path('', include(router.urls)),
    path('', CitizenView.as_view(), name="citizen_list"),
    path('gender/<str:slug>/', CitizenSearchView.as_view(),
         name="citizen_search_list"),
    path('religion/', ReligionCountView.as_view(), name='religion_count'),
    path('gender/', GenderCount.as_view(), name='gender_count'),
    path('ward/gender/', WardGenderCount.as_view(), name='ward_gender_count'),
    path('ward/religion/', WardReligionCount.as_view(),
         name='ward_religion_count'),
    path('literacy/', LiteracyCount.as_view(), name='literacy_count'),
    path('ward/literacy/', WardLiteracyCount.as_view(), name='literacy_count'),
]
