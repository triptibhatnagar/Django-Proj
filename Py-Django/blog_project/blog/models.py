from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Blog(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blogs')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # cached counter for quick display
    views_count = models.PositiveIntegerField(default=0)


def _str_(self):
    return self.title


def get_absolute_url(self):
    return reverse('blog-detail', kwargs={'pk': self.pk})

class BlogView(models.Model):

    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='views')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    viewed_at = models.DateTimeField(auto_now_add=True)


class Meta:
    unique_together = ('blog', 'user')
    ordering = ['-viewed_at']


def _str_(self):
    return f"{self.user.username} viewed {self.blog.title}"