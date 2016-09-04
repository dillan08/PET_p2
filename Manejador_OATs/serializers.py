from rest_framework import serializers
from .models import OAT

class OATSerializer(serializers.ModelSerializer):
    class Meta:
        model = OAT
        fields = ('id', 'nombre', 'descripcion', 'src_image')


"""
    Usando serializadores crudos
"""
"""
from rest_framework import serializers
from .models import OAT

class OATSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    nombre = serializers.CharField(required=True, allow_blank=False, max_length=20)
    descripcion = serializers.CharField(required=True, allow_blank=False, max_length=50)
    fecha_publicacion = serializers.DateTimeField(required=True)
    src_image = serializers.CharField(required=True, allow_blank=True, max_length=255)

    def create(self, validated_data):
        return OAT.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.nombre = validated_data.get('nombre', instance.nombre)
        instance.descipcion = validated_data.get('descripcion', instance.descipcion)
        instance.fecha_publicacion = validated_data.get('fecha_publicacion', instance.fecha_publicacion)
        instance.src_image = validated_data.get(instance.src_image)
        instance.save()
        return instance
"""
