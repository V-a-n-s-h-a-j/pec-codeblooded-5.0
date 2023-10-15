from django.db import models

# Create your models here.
class User(models.Model):
    name= models.CharField(max_length=50)
    password= models.CharField(max_length=15)
    dob= models.DateField(null=True)

    def __str__(self):
        return str(self.name) 