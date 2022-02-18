from .models import Task , Member, Case # import models
from rest_framework import serializers # import serializers



class TaskSerializer(serializers.ModelSerializer):
    """
    Serializer for Task model
    """
    class Meta:
        """ 
        Meta class for TaskSerializer -- 
        """        
        model = Task # get the model
        fields = ('task', 'task_priority', 'date_from', 'date_to', 'assign_member') # get the fields
    

class MemberSerializer(serializers.ModelSerializer):
    """
    Serializer for Member model
    """
    class Meta:
        """
        Meta class for MemberSerializer --
        """
        model = Member # get the model
        fields = ('name', 'section') # get the fields

class CaseSerializer(serializers.ModelSerializer):
    """
    Serializer for Case model
    """
    class Meta:
        """
        Meta class for CaseSerializer --
        """
        model = Case # get the model
        fields = ('petition_number', 'parties', 'assigning_unit', 'connected_cases', 'case_priority', 'other_contributors') # get the fields