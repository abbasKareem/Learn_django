from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Item
from .serializers import ItemSerializer


class Index(APIView):
    def get(self, request):
        qs = Item.objects.all()
        serializer = ItemSerializer(qs, many=True)
        return Response(serializer.data, status=200)


