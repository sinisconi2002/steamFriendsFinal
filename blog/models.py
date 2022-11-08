from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = RichTextField(blank=True, null=True)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(default='static/media/blog/posts/1280px-CFR_050_locomotive.jpg', upload_to='static/media/blog/posts')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('postdetailed', kwargs={'pk': self.pk})
