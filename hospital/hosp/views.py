from django.shortcuts import render

from rest_framework import viewsets

from .models import Department, Patient
from .serializers import DepartmentSerializer, PatientSerializer


# Create your views here.

class DepartmentAPIViewSet(viewsets.ModelViewSet):
    """ViewSet для отображения отделений стационара"""
    serializer_class = DepartmentSerializer

    def get_queryset(self):
        queryset = Department.objects.all()
        return queryset


class AllPatientAPIViewSet(viewsets.ModelViewSet):
    """ViewSet для отображения всех пациентов стационара за все время"""
    serializer_class = PatientSerializer

    def get_queryset(self):
        queryset = Patient.objects.all()
        return queryset


class PatientSickAPIViewSet(viewsets.ModelViewSet):
    """ViewSet для отображения пациентов находящихся в стационаре"""
    serializer_class = PatientSerializer

    def get_queryset(self):
        queryset = Patient.objects.filter(is_discharge=False)
        return queryset


class PatientDischargeAPIViewSet(viewsets.ModelViewSet):
    """ViewSet для отображения выписанных пациентов стационара"""
    serializer_class = PatientSerializer

    def get_queryset(self):
        queryset = Patient.objects.filter(is_discharge=True)
        return queryset
