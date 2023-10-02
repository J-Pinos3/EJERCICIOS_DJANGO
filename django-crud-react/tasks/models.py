from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=200) 
    description = models.TextField(blank=True) 
    done = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Tasks'

    #para que en el django admin,
    #la tarea se muestre como <titulo de la tarea>
    def __str__(self) -> str:
        return self.title