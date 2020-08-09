from django.urls import path,include
from . import views
from rest_framework import routers


router1=routers.DefaultRouter()
router1.register('user',views.userdata)
router2=routers.DefaultRouter()
router2.register('content',views.contentdata)

urlpatterns = [
    path("",views.home,name="home"),
    path("input",views.input,name="input"),
    path("data",views.data,name="data"),
    path("",include(router1.urls)),
    path("",include(router2.urls)),
    path("sixdata",views.sixdata,name="sixdata"),

]
