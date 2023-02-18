from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from location.views import RecyclingLocationList

urlpatterns = [
    path('admin/', admin.site.urls),
    path('recycling-locations/', RecyclingLocationList.as_view()),
]
