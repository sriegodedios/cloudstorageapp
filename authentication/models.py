from django.db import models
from django import forms

# Create your models here
class Users(models.Model):
    firstname = models.TextField()
    lastname = models.TextField()
    username = models.TextField(unique=True)
    email = models.TextField(unique=True)
    password = forms.CharField(max_length=50, widget=forms.PasswordInput)
    accesstype = models.IntegerField()
    enabled = models.BooleanField()
    code = models.IntegerField(blank=True, null=True)
    created_on = models.DateTimeField()
    updated_on = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'users'