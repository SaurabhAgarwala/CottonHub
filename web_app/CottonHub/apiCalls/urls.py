from django.conf.urls import url, include
from . import views
from django.urls import path

urlpatterns = [
    url(r'^$',views.redirectToLoginOrDashboard),
    url(r'^login/',views.login),
    url(r'^logout/',views.logout),
    url(r'^otplogin/',views.otpLogin),
    url(r'^signup/',views.signUp),
    url(r'^dashboard',views.dashboard),
    url(r'^profile',views.profile),
    url(r'^faq',views.faq),
    url(r'^getfaq', views.getFaq),
    url(r'^feedback',views.feedback),
    url(r'^privacypolicy',views.privacypolicy),
    url(r'^updateprofile',views.updateProfile),
    url(r'^getorders',views.getOrders),
    url(r'^getmarket',views.getMarket),
    url(r'^inventory',views.Inventory),                # for getting all inventory in json
    url(r'^userinventory',views.getInventoryDetails),     # for showing user inventory on template
    url(r'^getinventory',views.getInventoryOfUser),    # for getting user inventory in json
    url(r'^getcottontypes',views.getCottonDetails),
    url(r'^getcottontypeanalysis',views.getAllTypeCottonAnalysis),
    url(r'^cart',views.cart),
    url(r'^buy',views.buyProduct),
    url(r'^sell',views.sellProduct),
    url(r'^analysis',views.analysis),
    url(r'^getanalysis',views.getAnalysis),
    url(r'^orderhistory',views.orderHistory),
    url(r'^getheatmap',views.getHeatMap),
    path('deleteorder/<int:id>', views.deleteOrder),
    path('placeorder/<int:id>', views.placeOrder),
    path('deleteinventory/<int:id>', views.deleteInventory),
]