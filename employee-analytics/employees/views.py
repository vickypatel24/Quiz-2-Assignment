from rest_framework import generics
from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.db.models import Avg, Max, Min, Count
from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from django.db.models import Avg, Max, Min, Count
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
import logging
from django.http import JsonResponse
import csv
from django.http import HttpResponse

logger = logging.getLogger(__name__)


def handler404(request, exception):
    logger.error(f"404 Error: Page not found - {request.path}")
    return render(request, '404.html', status=404)


class MyTokenObtainPairView(TokenObtainPairView):
    pass


class MyTokenRefreshView(TokenRefreshView):
    pass


class EmployeeListAPIView(generics.ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    filter_backends = [DjangoFilterBackend]

    filterset_fields = ['department', 'position']
    # permission_classes = [IsAuthenticated]


@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def employee_summary(request):
    try:
        logger.info(
            f"Request: {request.method} {request.path} from {request.META.get('REMOTE_ADDR')}")
        summary = Employee.objects.aggregate(
            avg_salary=Avg('salary'),
            max_salary=Max('salary'),
            min_salary=Min('salary'),
            total_employees=Count('id')
        )
        return Response(summary)
    except Exception as e:
        logger.error(f"Error occurred: {str(e)}")
        return Response({"error": "Internal Server Error"}, status=500)


def chart_view(request):
    return render(request, 'chart.html')

# ---------------------- To export employee data to a CSV file-----------------------

# with this ------------------url http://localhost:8000/api/export/csv/     ----------------


def export_employees_csv(request):
    # Create the HTTP response with the correct content type for CSV
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="employees.csv"'

    writer = csv.writer(response)
    writer.writerow(['First Name', 'Last Name', 'Department', 'Salary'])

    # Fetch all employees from the database
    employees = Employee.objects.all()
    for employee in employees:
        writer.writerow([employee.first_name, employee.last_name,
                        employee.department, employee.salary])

    return response
