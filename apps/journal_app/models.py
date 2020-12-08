from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
FORM_NAME_REGEX = re.compile(r'^[a-zA-Z- ]+$')

#UserManager will be used to validate users upon login and registration.
class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['name']) < 2:
            errors["name"] = "Name must be at least 2 characters."

        if len(postData['alias']) < 2:
            errors["alias"] = "Alias must be at least 2 characters."

        if int(postData['age']) < 16:
            errors['age'] = "Must be at least 16 years old to create an account."

        if int(postData['age']) > 130:
            errors['age'] = "You are not that old. ;)"

        if len(postData['email']) < 5:
            errors["email"] = "Email must be at least 5 characters."

        emails = User.objects.filter(email=postData["email"])
        if emails:
            errors["email"] = "Email address already exists."

        if len(postData['password']) < 8:
            errors["password"] = "Password must be at least 8 characters."

        if postData['password'] != postData['confirm_password']:
            errors["password"] = "Password fields must match."

        return errors

class MorningManager(models.Manager):
    def morning_validator(self, postData):
        errors = {}

class User(models.Model):
    name = models.CharField(max_length=45)
    alias = models.CharField(max_length=45)
    age = models.IntegerField(validators=[MinValueValidator(16), MaxValueValidator(130)])
    email = models.CharField(max_length=60)
    password = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class Day(models.Model):
    date = models.DateField(auto_now_add=True)
    page = models.PositiveIntegerField()
    quote = models.CharField(max_length=60)
    quote_author = models.CharField(max_length=60)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE, 
        related_name="days"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Morning(models.Model):
    day = models.OneToOneField(
        Day,
        on_delete = models.CASCADE,
        primary_key = True,
        related_name = "morning"
    )
    grateful_first = models.CharField(max_length=60)
    grateful_second = models.CharField(max_length=60)
    grateful_third = models.CharField(max_length=60)
    great_first = models.CharField(max_length=60)
    great_second = models.CharField(max_length=60)
    great_third = models.CharField(max_length=60)
    affirmation = models.CharField(max_length=60)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Night(models.Model):
    day = models.OneToOneField(
        Day,
        on_delete = models.CASCADE,
        primary_key = True,
        related_name = "night"
    )
    amazing_first = models.CharField(max_length=60)
    amazing_second = models.CharField(max_length=60)
    amazing_third = models.CharField(max_length=60)
    made_better = models.CharField(max_length=60)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Thought(models.Model):
    day = models.OneToOneField(
        Day,
        on_delete = models.CASCADE,
        primary_key = True,
        related_name = "thought"
    )
    thought = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)