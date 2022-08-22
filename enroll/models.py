from django.db import models

# Create your models here.
class Employee(models.Model):
    name=models.CharField(max_length=50)
    age=models.IntegerField()
    add=models.CharField(max_length=100)
    sal=models.IntegerField()

    def _str_(self):
        return self.name + " " + self.add
