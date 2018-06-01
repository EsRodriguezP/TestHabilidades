from rest_framework import serializers
from .models import InfoBasica, InfoAdicional

class InfoAdicionalSerializer(serializers.ModelSerializer):

	class Meta:
		model = InfoAdicional
		fields = ('arte','cine','musica')


class InfoBasicaSerializer(serializers.ModelSerializer):

#	adicional =InfoAdicionalSerializer(many=True)

	class Meta:
		model = InfoBasica
		fields = ('id','nombres','apellidos','telefono','email','direccion',)
		
#	def create(self, validated_data):								Esta parte es para anidar los serilizers
#		adicional_data = validated_data.pop('adicional')
#		nomb = InfoBasica.objects.create(**validated_data)
#		for add_data in adicional_data:
#			InfoAdicional.objects.create(nomb=nomb, **add_data)
#		return nomb