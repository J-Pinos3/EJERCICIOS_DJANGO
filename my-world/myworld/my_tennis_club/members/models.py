from django.db import models

#THIS WILL BE A TABLE IN THE SQLITE3 DATABASE
class Member(models.Model):
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)

    phone = models.IntegerField(null=True)