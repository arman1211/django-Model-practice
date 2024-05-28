from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=20)
    id = models.IntegerField(primary_key=True)
    email = models.EmailField(max_length=254, unique=True)

    def __str__(self) -> str:
        return f'Roll: {self.id} -> {self.name}'


