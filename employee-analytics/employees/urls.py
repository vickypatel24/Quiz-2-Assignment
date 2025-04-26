from django.urls import path
from .views import *


handler404 = 'employees.views.handler404'


urlpatterns = [
    path('employees/', EmployeeListAPIView.as_view(), name='employee-list'),
    path('summary/', employee_summary, name='employee-summary'),
    path('chart/', chart_view, name='chart-view'),
    # path('token/', MyTokenObtainPairView.as_view(),
    #      name='token_obtain_pair'),  # Login
    # path('token/refresh/', MyTokenRefreshView.as_view(),
    #      name='token_refresh'),  # Refresh token
    path('export/csv/', export_employees_csv, name='export_employees_csv'),


]
