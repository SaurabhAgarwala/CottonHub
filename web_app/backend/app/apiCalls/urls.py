from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^login/',views.login),
    url(r'^logout/',views.logout),
    url(r'^otplogin/',views.otpLogin),
    url(r'^signup/',views.signUp),

]