from django.db import models
from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    uname = forms.CharField(max_length=30, label="username")
    pswd = forms.CharField(max_length=30, label="password")


class Contact(models.Model):
    fname = models.CharField(max_length=30, default=1)
    lname = models.CharField(max_length=3, default=1)
    email = models.EmailField(default=1)
    contact = models.IntegerField(default=1)
    msg = models.CharField(max_length=100, default=1)

    class Meta:
        db_table = "contact"


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"
