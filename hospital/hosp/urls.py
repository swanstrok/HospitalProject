from django.urls import path
from rest_framework import routers

from .views import DepartmentAPIViewSet, PatientDischargeAPIViewSet, PatientSickAPIViewSet, \
    AllPatientAPIViewSet

router = routers.DefaultRouter()
router.register(r'department', DepartmentAPIViewSet, basename='department')
router.register(r'patients/sick', PatientSickAPIViewSet, basename='sick_patients')
router.register(r'patients/discharged', PatientDischargeAPIViewSet, basename='discharged_patients')
router.register(r'patients', AllPatientAPIViewSet, basename='all_patients')

urlpatterns = [
    # path('patients/sick/', PatientSickAPIViewSet),
    # path('patients/discharged/', PatientDischargeAPIViewSet)
]

urlpatterns += router.urls
