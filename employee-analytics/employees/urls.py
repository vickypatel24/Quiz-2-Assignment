from django.urls import path
from .views import EmployeeListAPIView, employee_summary

urlpatterns = [
    path('employees/', EmployeeListAPIView.as_view(), name='employee-list'),
    path('summary/', employee_summary, name='employee-summary'),
]
