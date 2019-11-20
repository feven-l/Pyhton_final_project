from django.db import models
import re
from datetime import datetime

class UserManager(models.Manager):
    def reg_validator(self, postData):
        errors = {}
        if len(postData['first_name']) < 2:
            errors['first_name'] = "First name has to be more than two charachters"
        if len(postData['last_name']) < 2:
            errors['last_name'] = "last name has to be more than two charachters"
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):          
            errors['email'] = ("Invalid email address")
        if len(postData['password']) < 8:
            errors['password'] = "Password has to be more than eight charachters"
        if len(postData['confirm_pw']) < 8:
            errors['confrim_pw'] = "Password has to be more than eight charachters"
        # if postData['email']:
        #     errors['email'] = 'This email already exists.'
        return errors
    def log_validator(self, postData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):          
            errors['email'] = ("Invalid email address")
        if len(postData['password']) < 8:
            errors['password'] = "Password has to be more than eight charachters"
        return errors
        

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=115)
    birthday = models.DateField()
    password = models.CharField(max_length=255)
    confirm_pw = models.CharField(max_length=255)
    objects = UserManager()
    