from django.urls import path
from . import views # efcc/urls.py

urlpatterns = [
    path('task/', views.TaskList.as_view()), # list all tasks
    path('task/<int:pk>/', views.TaskDetail.as_view()), # pk is primary key
    path('member/', views.MemberList.as_view()), # list all members
    path('member/<int:pk>/', views.MemberDetail.as_view()), # pk is primary key
    path('case/', views.CaseList.as_view()), # list all cases
    path('case/<int:pk>/', views.CaseDetail.as_view()), # pk is primary key

]
