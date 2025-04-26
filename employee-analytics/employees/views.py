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


class MyTokenObtainPairView(TokenObtainPairView):
    pass  

class MyTokenRefreshView(TokenRefreshView):
    pass


class EmployeeListAPIView(generics.ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['department', 'position']  # You can filter by department or position
    permission_classes = [IsAuthenticated]



@api_view(['GET'])
@permission_classes([IsAuthenticated])  # <-- Add this line
def employee_summary(request):
    summary = Employee.objects.aggregate(
        avg_salary=Avg('salary'),
        max_salary=Max('salary'),
        min_salary=Min('salary'),
        total_employees=Count('id')
    )
    return Response(summary)


def chart_view(request):
    return render(request, 'chart.html')
