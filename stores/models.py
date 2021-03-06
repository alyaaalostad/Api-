from django.db import models

class Store(models.Model):
	name = models.CharField(max_length=255)
	description = models.TextField()
	added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name