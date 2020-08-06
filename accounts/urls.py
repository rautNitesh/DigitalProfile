from django.urls import path
from .views import UserLoginView, SimpleView, SignUpView, PasswordChangeView,\
    PasswordChangeRequestView, PasswordResetChangeView

urlpatterns = [
    path('', UserLoginView.as_view(), name='login'),
    path('simple/', SimpleView.as_view(), name='simple'),
    path('signup/', SignUpView.as_view(), name='register'),
    path('password-change/', PasswordChangeView.as_view(), name='change_password'),
    path('password-change-request/', PasswordChangeRequestView.as_view(), name='change_password'),
    path('password-change-reset/<token>/', PasswordResetChangeView.as_view(), name='change_password_reset'),
]
