from django.db import models


# Create your models here.
class Track(models.Model):
    track_id = models.AutoField(primary_key=True)
    track_name = models.CharField(max_length=50, default="")


class Student(models.Model):
    std_id = models.AutoField(primary_key=True)
    std_fname = models.CharField(max_length=20, default="")
    std_lname = models.CharField(max_length=20, default="")
    track_id = models.ForeignKey('Track', on_delete=models.CASCADE, default="")


class MyUser(models.Model):
    usr_id = models.AutoField(primary_key=True)
    usr_name = models.CharField(max_length=30, default="")
    usr_email = models.CharField(max_length=100, default="")
    usr_password = models.CharField(max_length=35)
    usr_is_logged = models.BooleanField(default=False)
