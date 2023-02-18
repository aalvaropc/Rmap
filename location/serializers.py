from rest_framework import serializers
from .models import RecyclingLocation

class RecyclingLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecyclingLocation
        fields = ['id', 'name', 'address', 'latitude', 'longitude', 'created_at', 'updated_at']