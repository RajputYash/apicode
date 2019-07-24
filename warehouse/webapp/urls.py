from django.conf.urls import url,include
from .views import LoginApi , TokenViewSet,CustomerViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'tokens', TokenViewSet)
router.register(r'customers', CustomerViewSet)



urlpatterns=[
    url('',include(router.urls)),
    url(r'^login/',LoginApi.as_view()),

    #url(r'^logout/',TokenViewSet.as_view())
    #url(r'token',token_create)
]