from django import forms
from .models import *



class UserRegForm(forms.ModelForm):
  
    class Meta:
        model = UserReg
        fields = ['user_id','middle_name','sex','age',]
        

class EventForm(forms.ModelForm):

    
    class Meta:
        model = Event
        fields = ['title', 'description','venue', 'date','start_time','end_time','category', ]