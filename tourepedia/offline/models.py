from django.db import models
from datetime import datetime

class TourInfo(models.Model):
	tour_name = models.CharField(max_length= 1024, null= True)
	tour_date = models.DateTimeField(null=True)
	number_of_adult = models.IntegerField(null=True)
	number_of_child = models.IntegerField(null=True)

	budget = models.IntegerField(null=True)
	needs = models.TextField(max_length=2048, null=True)
	def __str__(self):
		return self.tour_name


class Meeting(models.Model):
	tourinfo= models.ForeignKey(TourInfo, null=True)
	Meeting_date = models.DateTimeField(null=True)
	Meeting_attended_by = models.CharField(max_length=1024, null= True)
	Meeting_Result = models.CharField(max_length=1024, null =True)

		
class Deal(models.Model):
	tourinfo= models.ForeignKey(TourInfo, null=True)
	Deal_done = models.CharField(max_length=1024,null= True)


class Operation(models.Model):
	tourinfo= models.ForeignKey(TourInfo, null=True)
	Intercity_travel = models.CharField(max_length=1024, null= True)
	Local_travel = models.CharField(max_length=1024, null=True)

	hotel_name = models.CharField(max_length=1024, null=True)
	sightseeing = models.CharField(max_length=1024, null= True)

	extraordinery_point = models.CharField(max_length=1024, null=True)
	extra= models.CharField(max_length=1024, null=True)
		


		
# Create your models here.
