from .models import Item
from rest_framework.serializers import ModelSerializer


class ItemSerializer(ModelSerializer):
    class Meta:
        model = Item
        
        fields = ['created_by','id', 'name', 'price', 'description', 'countInStock', 'is_published']
    
