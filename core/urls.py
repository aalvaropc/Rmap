from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from location.views import RecyclingLocationList
from user.views import RegisterView, LoginView
from rest_framework import routers, serializers, viewsets
from rest_framework_simplejwt import views as jwt_views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('recycling-locations/', RecyclingLocationList.as_view()),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
]