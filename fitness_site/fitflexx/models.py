from django.db import models
from django.contrib.auth.models import AbstractUser


# User Registration and Login System

class User(AbstractUser):
    # Add any additional fields you need for your user model
    # For example:
    phone_number = models.CharField(max_length=20)

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    # Add additional fields for the user's profile
    # For example:
    bio = models.TextField()
    profile_image = models.ImageField(upload_to='profile_images/')
    # ...


# Class Booking System
class Class(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    # Add other fields specific to a class
    # For example:
    instructor = models.CharField(max_length=100)
    schedule = models.DateTimeField()
    # ...


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    booked_class = models.ForeignKey(Class, on_delete=models.CASCADE)
    booking_date = models.DateTimeField(auto_now_add=True)
    # ...


# Notification and Reminder
class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    # ...


class Reminder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reminder_date = models.DateTimeField()
    reminder_message = models.TextField()
    # ...


class ClassSchedule(models.Model):
    class_item = models.ForeignKey(Class, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    # ...
