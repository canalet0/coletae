from django.shortcuts import render
from rest_framework import generics
from .serializers import CollectionPointSerializer
from .models import CollectionPoint
from django.views import View

class Home(View):
    def get(self,request):
        result = {}
        return render(request, 'home/home.html',result)

class CollectionPointList(generics.ListCreateAPIView):
    queryset = CollectionPoint.objects.all()
    serializer_class = CollectionPointSerializer

class CollectionPointMaintenance(generics.RetrieveUpdateDestroyAPIView):
    queryset = CollectionPoint.objects.all()
    serializer_class = CollectionPointSerializer

class CollectionPoint(View):
    def get(self,request):
        result = {}
        return render(request, 'collectionPoints/collectionPoints.html',result)

class EditDetailCollectionPoint(View):
    def get(self,request):
        print('aeeeeeeeeeeeeeeeee')
        result = {}
        return render(request, 'collectionPoints/collectionPointMaintenance.html',result)