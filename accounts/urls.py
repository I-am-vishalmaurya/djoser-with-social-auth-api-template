from django.urls import path, include
from djoser import views as djoser_views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenVerifyView, TokenRefreshView

from accounts.views import RedirectSocial

urlpatterns = [
    path('auth/register/', djoser_views.UserViewSet.as_view({'post': 'create'}), name='register'),

    path('auth/account/info/', djoser_views.UserViewSet.as_view({'get': 'me'}), name='me'),
    path('auth/profile/', RedirectSocial.as_view()),

    path('auth/social/', include('djoser.social.urls')),
    path('auth/account/change-password/', djoser_views.UserViewSet.as_view({'post': 'set_password'}),
         name='reset-password'),

    path('auth/activate/', djoser_views.UserViewSet.as_view({'post': 'activation'}), name='activate'),
    path('auth/resend-activation-link/', djoser_views.UserViewSet.as_view({'post': 'resend_activation'}),
         name='resend-activation'),

    path('auth/account/delete/', djoser_views.UserViewSet.as_view({'delete': 'destroy'}), name='delete-account'),

    path('auth/token/create/', TokenObtainPairView.as_view(), name='login'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='refresh'),
    path('auth/token/verify/', TokenVerifyView.as_view(), name='verify'),
]
