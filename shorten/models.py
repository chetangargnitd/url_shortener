from django.db import models

# Create your models here.
class URLs(models.Model):
	shrinked_url = models.CharField(max_length=8, primary_key=True)
	original_url  = models.CharField(max_length=2083)
	created = models.DateTimeField(auto_now_add=True, blank = True)

	def __str__(self):
		return self.original_url
