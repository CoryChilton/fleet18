from django.db import models
from users.models import User
from events.models import Event

# Create your models here.

class BlogPost(models.Model):
    title = models.CharField(max_length=150)
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    created_timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    event = models.ForeignKey(Event, on_delete=models.PROTECT)
