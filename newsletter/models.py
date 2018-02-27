from django.db import models
from ckeditor.fields import RichTextField


class NewsLetter(models.Model):
    title = models.CharField(max_length=150)
    content = RichTextField()
    published = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    sort = models.IntegerField(default=9999)
    author = models.ForeignKey('auth.User')

    class Meta:
        ordering = ('-sort',)

    def __str__(self):
        return self.title


class Comment(models.Model):
    name = models.CharField(max_length=50, default='Guest')
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    newsletter = models.ForeignKey(NewsLetter, blank=False)


class Recipient(models.Model):
    first = models.CharField(max_length=100)
    last = models.CharField(max_length=100)
    email = models.EmailField()
    subscribed = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.first + ' ' + self.last
