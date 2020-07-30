from django.urls import path
from .views import UserLoginView, SimpleView, SignUpView

urlpatterns = [
    path('', UserLoginView.as_view(), name='login'),
    path('simple/', SimpleView.as_view(), name='simple'),
    path('signup/', SignUpView.as_view(), name='register'),
]
