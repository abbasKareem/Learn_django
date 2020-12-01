from rest_framework.response import Response
from django.shortcuts import redirect
from django.http import HttpResponse
from rest_framework.views import APIView
from .models import Item
from .serializers import ItemSerializer


class Index(APIView):
    def get(self, request):
        items = Item.objects.all()
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data, status=200)

    def post(self, request, format=None):
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    
class IndexDetails(APIView):
    def get(self, request, pk):
        try:
            itemToGet = Item.objects.get(id=pk)
            if itemToGet:
                serializer = ItemSerializer(itemToGet)
                return Response(serializer.data, status=200)
        except:
            return Response({'msg': 'Given Item object is not found'}, status=404)


    def delete(self, request, pk, format=None):
        try:
            itemToDeleted = Item.objects.get(id=pk)
            if itemToDeleted:
                itemToDeleted.delete()
                return Response({'msg': 'DELETED'}, status=202)
        except:
            return Response({'msg': 'Given Item object is not found'}, status=404)




    # queryset = Item.objects.all()
    # serializer_class = ItemSerializer

