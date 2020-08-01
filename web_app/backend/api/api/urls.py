from django.urls import path, include
from django.conf.urls import url, include
from . import views
from rest_framework import routers

urlpatterns = [
    
    url(r'^auth/',include('djoser.urls')),
    url(r'^auth/', include('djoser.urls.authtoken')),
    url(r'^otplogin',views.otpLogin),
    url(r'^verifyotp',views.verifyOTP),
    url(r'^',include(router.urls)),    
]