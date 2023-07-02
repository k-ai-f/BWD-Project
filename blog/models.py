from django.db import models
from tinymce.models import HTMLField
from django.contrib.auth.models import User

class Article(models.Model):
	title = models.CharField(max_length=255)
	content = HTMLField()
	date = models.DateField(auto_now_add=True)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	featured = models.BooleanField(default=False)
	likes = models.ManyToManyField(User, related_name='likes', blank=True)
	
class Comments(models.Model):
	post = models.ForeignKey(Article,related_name='comments', on_delete=models.CASCADE)
	name = models.CharField(max_length=255)
	body = models.TextField()
	date_added = models.DateTimeField(auto_now_add=True)
	
	def __str__(self):
		return '%s  - %s' %(self.post.title, self.name)
    