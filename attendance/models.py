from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
user= get_user_model()

class Attendance(models.Model):
    user= models.ForeignKey(user, 
                             related_name="attendance",
                             on_delete=models.CASCADE)
    checkin_date= models.DateField()
    checkin_time= models.TimeField()
    checkout_time = models.TimeField(blank=True, null=True)
    



