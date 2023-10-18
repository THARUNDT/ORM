from django.db import models
from django.contrib import admin
class Football_player (models.Model):
    name=models.CharField(max_length=20)
    age=models.IntegerField()
    country=models.CharField(max_length=20)
    height=models.IntegerField()
    email=models.EmailField()

class Football_playerAdmin(admin.ModelAdmin):
    list_display=['name','age','country','height','email']

 