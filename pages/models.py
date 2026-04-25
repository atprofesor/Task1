from django.db import models
from django.urls import reverse
from django.utils import timezone

# Create your models here.
class post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()


class Article(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100) # Opcional por ahora
    content = models.TextField()
    published_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("article_detail", kwargs={"pk": self.pk})    