from django.db import models
from django.contrib.auth.models import User  

class Greeting(models.Model):
    text = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, db_index=True, on_delete=models.CASCADE)
