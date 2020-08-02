from django.urls import path, include
from django.conf.urls import url, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"order", views.OrderViewSet)
router.register(r"orderitem", views.OrderItemViewSet)
router.register(r"cottontype", views.CottonTypeViewSet)
router.register(r"market", views.MarketViewSet)
router.register(r"product", views.ProductViewSet)
router.register(r"inventory", views.InventoryViewSet)

urlpatterns = [
    url(r"^auth/", include("djoser.urls")),
    url(r"^auth/", include("djoser.urls.authtoken")),
    url(r"^otplogin", views.otpLogin),
    url(r"^verifyotp", views.verifyOTP),
    url(r"^", include(router.urls)),
]
