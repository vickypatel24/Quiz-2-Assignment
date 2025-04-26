from rest_framework import generics
from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.db.models import Avg, Max, Min, Count


class EmployeeListAPIView(generics.ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


@api_view(['GET'])
def employee_summary(request):
    summary = Employee.objects.aggregate(
        avg_salary=Avg('salary'),
        max_salary=Max('salary'),
        min_salary=Min('salary'),
        total_employees=Count('id')
    )
    return Response(summary)
