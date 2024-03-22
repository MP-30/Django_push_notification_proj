from django.contrib import admin

from django import forms
from django.http import HttpRequest
from django.http.response import HttpResponse
from .models import Notification

class SecondNotificationForm(forms.Form):
    message = forms.CharField(label = "Notification Mesasge", max_length=200)
    
@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    add_form_template = "admin/custon_add_form.html"
    
    def add_view(self, request, form_url="", extra_context= None):
        if request.method == "POST":
            form = SecondNotificationForm(request.POST)
            if form.is_valid():
                message = form.cleaned_data["message"]
                
                notification = Notification.objects.create(message = message)
                
            else:
                form = SecondNotificationForm()
                
            context = self.get_changeform_initial_data(request)
            context["form"] = form
            return super().add_view(request, form_url, extra_context=context)
