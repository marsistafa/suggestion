from django.db import models

class Suggestion(models.Model):
    category = models.CharField(max_length=255)
    description = models.TextField()
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)
