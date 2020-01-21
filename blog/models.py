from django.db import models
from django.utils import timezone                                   # for Post.date_posted attribute (allows date modification)
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length = 100)
    content = models.TextField()
    date_posted = models.DateTimeField(default = timezone.now)
    author = models.ForeignKey(User, on_delete = models.CASCADE)    # If user deleted, that user's posts are deleted too

    def __str__(self):
        return self.title

