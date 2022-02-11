from django.db import models


class Document(models.Model):
    ticket_id=models.CharField(max_length=255, unique=True)
    content = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    topic = models.CharField(max_length=255, blank=True)
    author = models.CharField(max_length=255)
    water_mark = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title
