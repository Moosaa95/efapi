from django.db import models


# create task
# task 
# task priority 
# data (from - to )
# assign member

class Task(models.Model):
    """ 
    Task model
    fields for task database
    fields ---> 
        task - char
        task_priority - char
        date_from - date
        date_to - date
        assign_member - char
    """
    task = models.CharField(max_length=200)
    task_priority = models.CharField(max_length=200)
    date_from = models.DateField()
    date_to = models.DateField()
    assign_member = models.CharField(max_length=200)

    def __str__(self):
        return self.task


class Member(models.Model):
    """
    Member model
    fields for member database
    fields ---> 
        name - char
        section - char
    """
    section_choice = (
        ('legal', 'legal'),
        ('investigation', 'investigation'),
        ('evidence', 'evidence'),
    )
    name = models.CharField(max_length=200)
    section = models.CharField(max_length=200, choices=section_choice)

    def __str__(self):
        return self.name

#adding case
# petition number
# parties 
# assigning unit (bank fraud, Economic Governance, counter-Terrorism and General investigation) -- drop down
#connected cases --empty
# case priority(dropdown )
#other contributors (legal dept, nitda)drowdown

class Case(models.Model):
    """
        fields for the database
        database fields --->
                    petition_number --- char
                    parties --- char
                    assigning_unit --- char
                    connected_cases --- char
                    case_priority --- char
                    other_contributors --- char

    """
    assigning_choices = (
        ('bank fraud', 'bank fraud'),
        ('Economic Governance', 'Economic Governance'),
        ('Counter', 'Counter-Terrorism and General investigation')
    ) # for drop down assigning
    case_priority_choices = (
        ('case #1', 'case #1' ),
    ) # for drop down case
    other_contributors_choices = (
        ('legal department', 'legal department'),
        ('nitda', 'nitda'),

    )
    petition_number = models.IntegerField()
    parties = models.CharField(max_length=200)
    assigning_unit = models.CharField(max_length=200, choices=assigning_choices)
    connected_cases = models.CharField(max_length=200)
    case_priority = models.CharField(max_length=200, choices=case_priority_choices)
    other_contributors = models.CharField(max_length=200, choices=other_contributors_choices)


