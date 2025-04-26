from django.core.management.base import BaseCommand
from employees.models import Employee
from faker import Faker
import random


class Command(BaseCommand):
    help = 'Generate synthetic employee data'

    def handle(self, *args, **kwargs):
        fake = Faker()
        departments = ['Engineering', 'HR', 'Sales', 'Marketing', 'Finance']

        for _ in range(100):  # Generate 100 employees
            Employee.objects.create(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                department=random.choice(departments),
                salary=round(random.uniform(30000, 120000), 2),
                joining_date=fake.date_between(
                    start_date='-10y', end_date='today')
            )
        self.stdout.write(self.style.SUCCESS(
            'Successfully generated employee data!'))
