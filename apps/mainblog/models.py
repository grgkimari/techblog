from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    dateCreated = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['dateCreated']

    def __str__(self) -> str:
        return "POST : " + self.title + " | " + str(self.author)

    def get_absolute_url(self):
        return reverse("article_view", args=(str(self.id)))
    
