from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    User = models.ForeignKey(User, on_delete= models.CASCADE)
    title = models.CharField(max_length=100, null = True)
    description = models.TextField()
    complete = models.BooleanField(default= False)
    created = models.DateTimeField(auto_now_add= True)

    def __str__(self):
        return self.title
