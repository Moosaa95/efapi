from .serializers import TaskSerializer, MemberSerializer, CaseSerializer
from rest_framework import generics
from .models import Task, Member, Case




class TaskList(generics.ListCreateAPIView):
    """
    List all tasks, or create a new task.
    

    Args:
        generics(): ListCreateAPIView
    """    
    queryset = Task.objects.all() # get all tasks from database
    serializer_class = TaskSerializer # serialize the data


class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a task instance.

    Args:
        generics (_type_): RetrieveUpdateDestroyAPIView
    """    
    queryset = Task.objects.all() # get all tasks from database
    serializer_class = TaskSerializer # serialize the data

class MemberList(generics.ListCreateAPIView):
    """
    List all members, or create a new member.
    """
    queryset = Member.objects.all() # get all members from database
    serializer_class = MemberSerializer # serialize the data


class MemberDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a member instance.
    """
    queryset = Member.objects.all() # get all members from database
    serializer_class = MemberSerializer # serialize the data

class CaseList(generics.ListCreateAPIView):
    """
    List all cases, or create a new case.
    """
    queryset = Case.objects.all() # get all cases from database
    serializer_class = CaseSerializer # serialize the data

class CaseDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a case instance.
    """
    queryset = Case.objects.all() # get all cases from database
    serializer_class = CaseSerializer # serialize the data



# create task
# task 
# task priority 
# data (from - to )
# assign member


# add member
# name
# select section(legal, investigation, evidence) drop down


#adding case
# petition number
# parties 
# assigning unit (bank fraud, Economic Governance, counter-Terrorism and General investigation) -- drop down
#connected cases --empty
# case priority(dropdown )
#other contributors (legal dept, nitda)drowdown




