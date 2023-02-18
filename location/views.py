from rest_framework.views import APIView
from rest_framework.response import Response
from .models import RecyclingLocation
from .serializers import RecyclingLocationSerializer

class RecyclingLocationList(APIView):
    def get(self, request):
        recycling_locations = RecyclingLocation.objects.all()
        serializer = RecyclingLocationSerializer(recycling_locations, many=True)
        return Response(serializer.data)
