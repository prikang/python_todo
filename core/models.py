from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
user= get_user_model()
class Todo(models.Model):
    user = models.ForeignKey(user, 
                             related_name="todo",
                             on_delete=models.CASCADE)
    title = models.CharField(max_length=127)
    description = models.TextField(blank=True,null=True)
    send_alret= models.BooleanField(default=False)
    date_time=models.DateTimeField()



class Profile(models.Model):
    user = models.OneToOneField(user, 
                             related_name="profile",
                             on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    phoneNumber= models.CharField(max_length=63)

