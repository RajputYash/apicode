from django.conf.urls import url,include
from .views import LoginApi, TokenViewSet, CustomerViewSet, ForgetPassword, ResetPasswordApi
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'tokens', TokenViewSet)
router.register(r'customers', CustomerViewSet)


urlpatterns = [

    url('', include(router.urls)),
    url(r'^login/', LoginApi.as_view()),
    url(r'^forgot/', ForgetPassword.as_view()),
    url(r'^reset/', ResetPasswordApi.as_view()),
]