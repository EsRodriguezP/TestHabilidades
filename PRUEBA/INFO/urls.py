from django.urls import path, include
from . import serializers
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('infobasica', views.InfoBasicaView)
router.register('infomas', views.InfoAdicionalView)

urlpatterns = [
	path('', include(router.urls))
]