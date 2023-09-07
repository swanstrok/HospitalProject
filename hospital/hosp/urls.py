from django.urls import path, include
from rest_framework import routers

from .views import DepartmentAPIViewSet, PatientDischargeAPIViewSet, PatientSickAPIViewSet, \
    AllPatientAPIViewSet

router = routers.DefaultRouter()
router.register(r'department', DepartmentAPIViewSet, basename='department')
router.register(r'patients/sick', PatientSickAPIViewSet, basename='sick_patients')
router.register(r'patients/discharged', PatientDischargeAPIViewSet, basename='discharged_patients')
router.register(r'patients', AllPatientAPIViewSet, basename='all_patients')

urlpatterns = [
    path('drf-auth/', include('rest_framework.urls')),
]

urlpatterns += router.urls
