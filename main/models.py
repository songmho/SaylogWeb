from django.db import models

# Create your models here.

class Saying(models.Model):
	saying_text = models.CharField(max_length=500)
	source_text = models.CharField(max_length=100)
	pub_date = models.DateTimeField('date published')
	def __str__(self):
		return self.saying_text
		