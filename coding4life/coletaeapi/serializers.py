from rest_framework import serializers
from .models import CollectionPoint

class CollectionPointSerializer(serializers.ModelSerializer):
    class Meta:
        model = CollectionPoint
        fields = ('name','address','addressComplement','uf','city','items')