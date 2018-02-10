from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100)
    post_text = models.TextField(null=True, blank=True)
    author = models.CharField(max_length=50)
    pub_date = models.DateTimeField('date published')




