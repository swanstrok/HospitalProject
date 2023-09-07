from rest_framework import serializers

from .models import Patient, Department


class DepartmentSerializer(serializers.ModelSerializer):
    """Сериализатор для класса Department"""

    class Meta:
        model = Department
        fields = '__all__'


class PatientSerializer(serializers.ModelSerializer):
    """Сериализатор для класса Patient"""

    class Meta:
        model = Patient
        fields = '__all__'
