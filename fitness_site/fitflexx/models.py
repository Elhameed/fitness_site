from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

# # Class Booking System
# class Class(models.Model):
#     name = models.CharField(max_length=100)
#     description = models.TextField()
#     instructor = models.CharField(max_length=100)
#     schedule = models.DateTimeField()
#     # ...

# class Booking(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     booked_class = models.ForeignKey(Class, on_delete=models.CASCADE)
#     booking_date = models.DateTimeField(auto_now_add=True)
#     # ...

# # Notification and Reminder
# class Notification(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     message = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     is_read = models.BooleanField(default=False)
#     # ...

# class Reminder(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     reminder_date = models.DateTimeField()
#     reminder_message = models.TextField()
#     # ...

# class ClassSchedule(models.Model):
#     class_item = models.ForeignKey(Class, on_delete=models.CASCADE)
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='class_schedules')
#     date = models.DateField()
#     start_time = models.TimeField()
#     end_time = models.TimeField()
#     # ...
