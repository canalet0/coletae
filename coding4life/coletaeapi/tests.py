from django.test import TestCase
from .models import *
from rest_framework.test import APIClient
from rest_framework import status
from rest_framework import serializers
from django.urls import reverse
from django.db import models
from .serializers import *

class ModelTestCase(TestCase):
    def model_can_create(self,testObject,model):
        print("\n Realizing model can create test for: ",model,"\n")
        self.old_count = model.objects.count()
        testObject.save()
        self.new_count = model.objects.count()
        self.assertNotEqual(self.old_count, self.new_count)

class CollectionPointModelTestCase(ModelTestCase):
    def test_create(self):
        self.model_can_create(CollectionPoint(name="test"),CollectionPoint)

class ViewTestCase(TestCase):
    url = ''
    maintenanceUrl = ''
    model = models.Model
    serializer = serializers.ModelSerializer

    def setUp(self):
        self.client = APIClient()

    def view_can_create(self,testData):
        print("\nRealizing View Can Create test for urlName: ",self.url,"\n")
        self.assertEqual(0,0)
        self.client = APIClient()
        self.response = self.client.post(
            reverse(self.url),
            testData,
            format="json")
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
    
    def view_can_get(self):
        print("\nRealizing View Can Get test for urlName: ",self.maintenanceUrl,"\n")
        getObjectInstance = self.model.objects.get()
        response = self.client.get(
            reverse(self.maintenanceUrl,
            kwargs={'pk': getObjectInstance.id}), format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, self.serializer(getObjectInstance).data)

    def view_can_update(self,testData):
        print("\nRealizing View Can Update test for urlName: ",self.maintenanceUrl,"\n")
        serializedData = self.serializer(testData).data
        response = self.client.put(
            reverse(self.maintenanceUrl, kwargs={'pk': testData.id}),
            serializedData, format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializedData)

    def view_can_delete(self):
        print("\nRealizing View Can Delete test for urlName: ",self.maintenanceUrl,"\n")
        deleteObjectInstance = self.model.objects.first()
        old_count = self.model.objects.count()
        response = self.client.delete(
            reverse(self.maintenanceUrl, kwargs={'pk': deleteObjectInstance.id}),
            format='json',
            follow=True)
        objectHasDeleted = self.model.objects.first()
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEquals(old_count - 1, self.model.objects.count())
        
class CollectionPointViewTestCase(ViewTestCase):
    url = 'CollectionPoint'
    maintenanceUrl = 'CollectionPointMaintenance'
    model = CollectionPoint
    serializer = CollectionPointSerializer
 
    def test_can_create_collection_point(self):
        self.view_can_create({'name': 'test 1'})
    def test_can_get_collection_point(self):
        CollectionPoint(name="test").save()
        self.view_can_get()
    def test_can_update_collection_point(self):
        testObject = CollectionPoint(name="test")
        testObject.save()
        testObject.name = "updated Name"
        self.view_can_update(testObject)
    def test_can_delete_collection_point(self):
        CollectionPoint(name="test").save()
        self.view_can_delete()