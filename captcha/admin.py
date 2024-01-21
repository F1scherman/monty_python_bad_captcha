from django.contrib import admin

# Register your models here.
from .models import CaptchaQuestion
admin.site.register(CaptchaQuestion)
