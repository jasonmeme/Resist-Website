import datetime
from django.db import models
from django.utils import timezone

# Create your models here.

class NewCampaign(models.Model):
	title = models.CharField(max_length=100)
	date = models.DateField()
	location = models.CharField(max_length=200)
	organizer = models.CharField(max_length=100)
	description = models.CharField(max_length=500, blank=True)
	pub_date = models.DateTimeField(default=timezone.now)
	attendees = models.IntegerField(default=0)
	
	def __str__(self):
		return self.title

