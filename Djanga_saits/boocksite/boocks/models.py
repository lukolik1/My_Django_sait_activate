from django.db import models
from django.urls import reverse

class Boocks(models.Model):
	title = models.CharField(max_length=100)
	picture = models.ImageField(upload_to="picture/%y/%m/%d/")
	author = models.TextField(max_length=50)
	content = models.TextField(blank=True)
	time_create = models.DateTimeField(auto_now_add=True)
	is_published = models.BooleanField(default=True)
	cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)

	def __str__(self):
		return self.title



	def get_absolute_url(self):
		return reverse('Boocks', kwargs={'boocks_id': self.pk})

class Category(models.Model):
	name = models.CharField(max_length=100, db_index=True)


	def __str__(self):
		return self.name


	def get_absolute_url(self):
		return reverse('category', kwargs={'cat_id': self.pk})

