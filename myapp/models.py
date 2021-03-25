from django.db import models
from django.utils import timezone
from datetime import datetime
from django.contrib.auth.models import User


# Create your models here.


class UserReg(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True)
    first_name = models.CharField(max_length = 50, blank = True, null = True)
    middle_name = models.CharField(max_length = 50, blank = True, null = True)
    last_name = models.CharField(max_length = 50, blank = True, null = True)
    sex = models.CharField(max_length = 10, blank = True, null = True)
    age = models.IntegerField(blank = True, null = True)
    email_address = models.CharField(max_length = 50, blank = True, null = True)
    birth_date = models.DateField(default = datetime.now(), null = True)
    birth_place = models.CharField(max_length = 50, blank = True, null = True)
    phone_number = models.IntegerField(blank = True, null = True)
    created_at = models.DateTimeField(default = timezone.now)

    
    class Meta:
        db_table = "UserReg"

class Organizer(models.Model):
    custom_user = models.ForeignKey(UserReg, on_delete=models.CASCADE, related_name='organizer')
    description = models.CharField(max_length = 500, blank = True, null = True)
    started_organizer_at = models.DateTimeField(default = timezone.now)

    class Meta:
        db_table = 'Organizer'

class Admin(models.Model):
    custom_user = models.ForeignKey(UserReg, on_delete=models.CASCADE, related_name='admin')
    started_admin_at = models.DateTimeField(default = timezone.now)

    class Meta:
        db_table = "Admin"
           
class Event(models.Model):
    title = models.CharField(max_length = 128, default = "", blank = True, null = True)
    date = models.CharField(max_length = 128, default = "", blank = True, null = True)
    start_time = models.CharField(max_length = 128, default = "", blank = True, null = True)
    end_time = models.CharField(max_length = 128, default = "", blank = True, null = True)
    description = models.CharField(max_length = 128, default = "", blank = True, null = True)
    street = models.CharField(max_length = 128, default = "", blank = True, null = True)
    barangay = models.CharField(max_length = 128, default = "", blank = True, null = True)
    city = models.CharField(max_length = 128, default = "", blank = True, null = True)
    province = models.CharField(max_length = 128, default = "", blank = True, null = True)
    upvotes = models.IntegerField(default = 0)
    venue = models.CharField(max_length = 128, default = "", blank = True, null = True)
    category = models.CharField(max_length = 32, default = "", blank = True, null = True)
    status_event = models.CharField(max_length = 32, default = "reviewing")
    created_at = models.DateField(default = timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    organizer_id = models.ForeignKey(Organizer, on_delete=models.CASCADE, related_name='handled_events', null=True, blank=True)
    
    class Meta:
        db_table = "Event"

    # status_event
    #   reviewing - to be reviewed by admin
    #   accepted - accepted by the admin
    #   denied - denied by the admin
    
class OrganizerEvent(models.Model):
    organizer_id = models.ForeignKey(Organizer, on_delete=models.CASCADE, related_name='handled_organizer_events')
    event_id = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='handled_by')
    roles = models.CharField(max_length = 64, default = "", blank = True, null = True)
    
    class Meta:
        db_table = "Organizer_Event"
        
class EventUser(models.Model):
    event_id = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='get_all_participants')
    user_id = models.ForeignKey(UserReg, on_delete=models.CASCADE, related_name='get_all_joined_events')
    has_voted = models.BooleanField(default=False)
    
    class Meta:
        db_table = "Event_User"

class EventNotification(models.Model):
    event_id = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='sent_notifications')
    user_id = models.ForeignKey(UserReg, on_delete=models.CASCADE, related_name='received_notifications')
    remind_at = models.DateTimeField(blank = True, null = True)
    remind_details = models.CharField(max_length = 128, default = "", blank = True, null = True)
    
    class Meta:
        db_table = "Event_Notification"
        
class Review(models.Model):
    event_id = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='get_all_reviews')
    user_id = models.ForeignKey(UserReg, on_delete=models.CASCADE, related_name='get_all_authored_reviews')
    message = models.CharField(max_length = 128, default = "", blank = True, null = True)
    created_at = models.DateField(default = timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = "Review"

class Request(models.Model):
    user_id = models.ForeignKey(UserReg, on_delete=models.CASCADE, related_name='sent_requests')
    event_id = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='received_requests', blank=True, null=True)
    user_type = models.CharField(max_length = 128, blank = True, null = True)
    request_type = models.CharField(max_length = 128, blank = True, null = True)
    status_request = models.CharField(max_length = 128, default = "reviewing")
    description = models.CharField(max_length = 128, default = "", blank = True, null = True)
    remarks = models.CharField(max_length = 128, default = "", blank = True, null = True)
    created_at = models.DateField(default = timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = "Request"