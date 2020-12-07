from django.db import models

# Create your models here.

class Todo(models.Model):

    name = models.CharField(max_length=100, blank=False)
    due_date = models.DateField()
    description = models.TextField(max_length=2000, blank=True)

    def __str__(self):
        return self.name
