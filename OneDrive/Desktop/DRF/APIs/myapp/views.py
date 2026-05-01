from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework import serializers, status, viewsets
from rest_framework.decorators import api_view

from .pagination import CustomPagination
from .serializer import StudentSerializer
from .models import Student, Employee
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView, Http404
from .serializer import EmployeeSerializer

from rest_framework import generics, mixins
from .models import Student
from .pagination import CustomPagination
from .filters import EmployeeFilter
from rest_framework.filters import SearchFilter,OrderingFilter

# Create your views here.
@api_view(['GET', 'POST'])
def index(request):
    if request.method=='GET':
        students=Student.objects.all()
        serializers=StudentSerializer(students,many=True)
        return Response(serializers.data,status=status.HTTP_200_OK)
    elif request.method=='POST':
        serializers=StudentSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_201_CREATED)
    return Response(serializers.errors,status=status.HTTP_405_METHOD_NOT_ALLOWED)




class StudentList(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    
@api_view(['GET', 'PUT', 'DELETE'])
def student_detail(request,pk):
    try:
        student=Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=='GET':
        serializers=StudentSerializer(student)
        return Response(serializers.data,status=status.HTTP_200_OK)
    elif request.method=='PUT':
        serializers=StudentSerializer(student,data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_200_OK)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method=='DELETE':
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
# class EmployeeList(APIView):
#     def get(self,request):
#         employees=Employee.objects.all()
#         serializers=EmployeeSerializer(employees,many=True)
#         return Response(serializers.data,status=status.HTTP_200_OK)
#     def post(self,request):
#         serializers=EmployeeSerializer(data=request.data)
#         if serializers.is_valid():
#             serializers.save()
#             return Response(serializers.data,status=status.HTTP_201_CREATED)
#         return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)

# class EmployeeDetail(APIView):
#     def get_object(self,pk):
#         try:
#             return Employee.objects.get(pk=pk)
#         except Employee.DoesNotExist:
#             raise Http404
#     def get(self,request,pk):
#         employee=self.get_object(pk)
#         serializers=EmployeeSerializer(employee)
#         return Response(serializers.data,status=status.HTTP_200_OK)
#     def put(self,request,pk):
#         employee=self.get_object(pk)
#         serializers=EmployeeSerializer(employee,data=request.data)
#         if serializers.is_valid():
#             serializers.save()
#             return Response(serializers.data,status=status.HTTP_200_OK)
#         return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
#     def delete(self,request,pk):
#         employee=self.get_object(pk)
#         employee.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# class EmployeeDetail(generics.GenericAPIView,mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin):
#     queryset=Employee.objects.all()
#     serializer_class=EmployeeSerializer
#     def get(self,request,pk):
#         return self.retrieve(request,pk)
#     def put(self,request,pk):
#         return self.update(request,pk)
#     def delete(self,request,pk):
#         return self.destroy(request,pk)
    

# class EmployeeList(generics.GenericAPIView,mixins.ListModelMixin,mixins.CreateModelMixin):
#     queryset=Employee.objects.all()
#     serializer_class=EmployeeSerializer
#     def get(self,request):
#         return self.list(request)
#     def post(self,request):
#         return self.create(request)
    

# class EmployeeListCreateView(generics.ListCreateAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer

# class EmployeeDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer
#     lookup_field = 'pk'

# class EmployeViewset(viewsets.ViewSet):
#     def list(self,request):
#         employees=Employee.objects.all()
#         serializers=EmployeeSerializer(employees,many=True)
#         return Response(serializers.data,status=status.HTTP_200_OK)
#     def  create(self,request):
#         serializers=EmployeeSerializer(data=request.data)
#         if serializers.is_valid():
#             serializers.save()
#             return Response(serializers.data,status=status.HTTP_201_CREATED)
#         return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
#     def retrieve(self,request,pk=None):
#         try:
#             employee=Employee.objects.get(pk=pk)
#         except Employee.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#         serializers=EmployeeSerializer(employee)
#         return Response(serializers.data,status=status.HTTP_200_OK)

class EmployeViewset(viewsets.ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
    pagination_class = CustomPagination
    filter_backends=[SearchFilter,OrderingFilter]
    ordering_fileds=['id']
    search_fields=['name','department']


# class EmployeeList(generics.ListCreateAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer
#     pagination_class = CustomPagination


