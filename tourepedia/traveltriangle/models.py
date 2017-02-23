from django.db import models
from datetime import datetime


from django.template.defaultfilters import slugify
from django.contrib.admin.widgets import AdminDateWidget

from django.contrib.auth.models import User

from hotels.models import Hotel, HotelPrice


class TripDetail(models.Model):
	user = models.ForeignKey(User, null=True)
	staff_name = models.CharField(null=True, max_length=250, blank=True)
	trip_id = models.PositiveIntegerField(unique=True, null=True)	
	number_of_adults = models.PositiveIntegerField(null=True, blank=True)
	number_of_children = models.PositiveIntegerField(null=True, blank=True)
	source = models.CharField(max_length=250, null=True, blank=True)
	places = models.CharField(max_length=250, blank=True)

	start_day = models.DateField(null=True, blank=True)
	#end_day = models.DateTimeField(default=datetime.now, null=True)

	trip_nights = models.PositiveIntegerField(null=True, blank=True)
	person_name = models.CharField(max_length=250, blank=True)

	email = models.EmailField(blank=True)
	mobile = models.CharField(max_length=255,null=True, blank=True)

	budget = models.PositiveIntegerField(null=True, blank=True)
	pub_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)

	def __str__(self):
		return self.person_name

class Itinerary(models.Model):
	#tripdetail = models.ForeignKey(TripDetail, null=True)
	
	place_name = models.CharField(max_length=255)
	slug = models.SlugField(null=True)

	def __str__(self):
		return self.place_name

	def save(self, *args, **kwargs):
		self.slug = slugify(self.place_name)
		super(Itinerary, self).save(*args, **kwargs)

class ItineraryDayWise(models.Model):
	#quote = models.ForeignKey(Quote, null=True)
	itinerary = models.ForeignKey(Itinerary, null=True)
	heading_day = models.CharField(max_length=255,)
	detail = models.TextField(max_length=10000)
	running_kms = models.PositiveIntegerField(null=True)
	night_stay = models.ForeignKey(Hotel,blank=True, null=True)

	def __str__(self):
		return self.heading_day



class Comment(models.Model):
	user = models.ForeignKey(User, null=True)
	tripdetail = models.OneToOneField(TripDetail)
	staff_name = models.CharField(null=True,max_length=250,blank=True)

	pub_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
	quoted_price = models.PositiveIntegerField(null=True)

	calculation = models.TextField(max_length=20000, blank=True, null=True)

	short_description = models.TextField(max_length=2000, null=True, blank=True)

	INTERESTED = (
		('Not Interested', 'Not Interested'),
		('Interested','Interested'),
		('Highly Interested','Highly Interested'),
		('Booked', 'Booked')
		)

	interested_status = models.CharField(max_length=250, choices=INTERESTED, null=True)

	TRIP_STATUS = (
		('Not Booked', 'Not Booked'),
		('Booked With Us', 'Booked With Us'),
		('Booked With TT' , 'Booked With TT'),
		('Booked With Others', 'Booked With Others'),
		('Trip Cancelled', 'Trip Cancelled'),
		)

	trip_status = models.CharField(max_length=250, choices=TRIP_STATUS, null=True)

	def __str__(self):
		return self.tripdetail.person_name

class CallDetail(models.Model):
	user = models.ForeignKey(User, null=True)
	tripdetail = models.ForeignKey(TripDetail)
	pub_date = models.DateTimeField(blank=True, null=True, auto_now_add=True)
	call_number = models.CharField(null=True, max_length=250)
	comment = models.TextField(max_length=1000,)
	#pub_date = models.DateTimeField(default=datetime.now, null=True)

	def __str__(self):
		return self.tripdetail.person_name