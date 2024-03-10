from django.contrib import admin

from django import forms
from .models import Notification

class SecondNotificationForm(forms.Form):
    message = forms.CharField(label = "Notification Mesasge", max_length=200)
    
@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    pass
