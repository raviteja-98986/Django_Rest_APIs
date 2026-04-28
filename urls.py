from django.contrib import admin
from django.urls import path,include
from .import views
from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register('employee',views.EmployeViewset,basename='employee')
urlpatterns = [
    path('student/',views.index,name='index'),
    path('student/<int:pk>/',views.student_detail,name='student_detail'),
    path('',include(router.urls)),
        # path('employee/',views.EmployeeListCreateView.as_view(),name='employee_list'),
        # path('employee/<int:pk>/',views.EmployeeDetailView.as_view(),name='employee_detail'),
]