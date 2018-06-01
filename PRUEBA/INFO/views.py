from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import generics
from .models import InfoBasica, InfoAdicional
from .serializers import InfoBasicaSerializer, InfoAdicionalSerializer

class InfoBasicaView(viewsets.ModelViewSet):
	queryset = InfoBasica.objects.all()
	serializer_class = InfoBasicaSerializer

class InfoAdicionalView(viewsets.ModelViewSet):
	queryset = InfoAdicional.objects.all()
	serializer_class = InfoAdicionalSerializer
