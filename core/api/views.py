from rest_framework.response import Response
from django.shortcuts import redirect
from django.http import HttpResponse
from rest_framework.views import APIView
from .models import Item
from .serializers import ItemSerializer
from rest_framework import generics
from rest_framework import mixins
from rest_framework.authentication import TokenAuthentication, SessionAuthentication, BaseAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly

# CSRF Token uses by sessions authentications


class IndexListGenerics(generics.ListAPIView,
                         mixins.ListModelMixin,
                          mixins.CreateModelMixin,
                          mixins.RetrieveModelMixin,
                          mixins.DestroyModelMixin,
                          mixins.UpdateModelMixin):
    serializer_class = ItemSerializer
    queryset = Item.objects.all()
    lookup_field = 'id'
    authentication_classes = [SessionAuthentication ,BaseAuthentication ,TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request,id=None):
        if id:
            return self.retrieve(request, id)
        else:
            return self.list(request)
        return self.list(request)
    
    def post(self, request):
        return self.create(request)
    
    def put(self, request, id=None):
        return self.update(request, id)
    
    def delete(self, request, id=None):
        return self.destroy(request, id)


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

    def put(self, request, pk):
        itemToPut = Item.objects.get(id=pk)
        serializer = ItemSerializer(itemToPut, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors(), status=400)


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

