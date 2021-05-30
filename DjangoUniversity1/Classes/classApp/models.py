from django.db import models

#defining the djangoClasses model

class djangoClasses(models.Model):
    title = models.CharField(max_length=60)
    CourseNumber = models.IntegerField()
    InstructorName = models.CharField(max_length=60)
    Duration = models.FloatField()

    def __str__(self): #changing the name of the instances to the course title name
        return self.title


