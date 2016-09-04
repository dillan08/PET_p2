from rest_framework import serializers
from ManejadorCursos.models import Cursos

class CursosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cursos
        fields = ('nombre', 'descripcion', 'noAlumnos', 'alumnos')

