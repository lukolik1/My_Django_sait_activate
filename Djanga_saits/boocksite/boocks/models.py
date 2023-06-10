from django.db import models

class Boocks(models.Model):
	title = models.CharField(max_length=100)
	picture = models.ImageField(upload_to="picture/%y/%m/%d/")
	author = models.TextField(max_length=50)
	content = models.TextField(blank=True)
	time_create = models.DateTimeField(auto_now_add=True)
	is_published = models.BooleanField(default=True)

	def __str__(self):
		return self.title
