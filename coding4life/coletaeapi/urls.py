from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import Home,CollectionPointList,CollectionPointMaintenance,CollectionPoint,EditDetailCollectionPoint

urlpatterns = {
    url(r'^collectionpoints/(?P<pk>[0-9]+)/$', CollectionPointMaintenance.as_view(), name="CollectionPointMaintenance"),
    url(r'^collectionpoints/$', CollectionPointList.as_view(), name="CollectionPointList"),
    url(r'^collectionpoint/$', CollectionPoint.as_view(), name="CollectionPoint"),
    url(r'^collectionpoint/edit/(?P<pk>[0-9]+)/$', EditDetailCollectionPoint.as_view(), name="EditDetailCollectionPoint"),
    url(r'^collectionpoint/create/$', EditDetailCollectionPoint.as_view(), name="EditDetailCollectionPoint"),
    url('', Home.as_view(), name='home'),
}

urlpatterns = format_suffix_patterns(urlpatterns)