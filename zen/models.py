from django.db import models


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()

    def publish(self):
        self.save()

    def __str__(self):
        return self.title