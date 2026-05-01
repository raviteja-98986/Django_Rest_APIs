import django_filters
from .models import Employee



class EmployeeFilter(django_filters.FilterSet):
    department=django_filters.CharFilter(field_name='department',lookup_expr='iexact')
    name=django_filters.CharFilter(field_name='name',lookup_expr='icontains')
    salary=django_filters.RangeFilter(field_name='salary',lookup_expr='iexact')
    class Meta:
        model = Employee
        fields=['department','name','id']