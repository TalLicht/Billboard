from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100)
    post_text = models.TextField(null=True, blank=True)
    author = models.CharField(max_length=50)
    pub_date = models.DateTimeField('date published')
    # def __str__(self):
    #     return self.title.__str__()+self.post_text.__str__()+self.author.__str__()



