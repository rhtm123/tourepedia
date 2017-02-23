from django.db import models

class Subscriber(models.Model):
	subscriber_email = models.EmailField()

	def __str__(self):
		return self.subscriber_email
# Create your models here.
