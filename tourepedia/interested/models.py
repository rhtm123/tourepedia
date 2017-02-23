from datetime import datetime

from django.db import models

from tours.models import TourDetail
from schooltrips.models import SchoolTourDetail
from places.models import PlaceDetail



class Interested(models.Model):
	name = models.CharField(max_length=250, null=True)
	place = models.CharField(max_length=250, null=True)
	email = models.CharField(max_length=250, null=True)
	mobile = models.CharField(max_length=250, null=True)
	#date = models.DateField(blank=True, auto_now_add=True)



class InterestedPeople(models.Model):
	tourdetail = models.ForeignKey(TourDetail, null=True)
	time_date = models.DateTimeField(default=datetime.now, blank=True)
	name = models.CharField(max_length=1024, null=True)
	email = models.EmailField(null=True, blank=True)
	mobile = models.CharField(null=True, max_length=12)

	def __str__(self):
		return self.name

class InterestedForSchool(models.Model):
	schooltour = models.ForeignKey(SchoolTourDetail, null=True)
	time_date = models.DateTimeField(default=datetime.now, blank=True)
	school_name = models.CharField(max_length=250)
	name = models.CharField(max_length=250, null=True)
	email = models.EmailField(null=True, blank=True)
	mobile = models.CharField(null=True, max_length=12)

	def __str__(self):
		return self.school_name


class InterestedForPlace(models.Model):
	placedetail = models.ForeignKey(PlaceDetail, null=True, blank=True)
	time_date = models.DateTimeField(default=datetime.now, blank=True)
	name = models.CharField(max_length=1024, null=True)
	email = models.EmailField(null=True, blank=True)
	mobile = models.CharField(null=True, max_length=12)

	def __str__(self):
		return self.name