from datetime import datetime
from django.db import models
from traveltriangle.models import TripDetail
from hotels.models import Hotel


class BookedTrip(models.Model):
	tripdetail = models.OneToOneField(TripDetail)
	quoted_price = models.PositiveIntegerField(null=True, blank=True)
	total_expences = models.PositiveIntegerField(null=True, blank=True)
	pub_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)

	def __str__(self):
		return self.tripdetail.person_name

class BookedCar(models.Model):
	tripdetail = models.ForeignKey(TripDetail, null=True)
	car_name = models.CharField(max_length=225,null=True)
	concerned_person = models.CharField(max_length=250, null=True)
	total_price = models.PositiveIntegerField(null=True)
	price_paid = models.PositiveIntegerField(null=True)
	pub_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)


class BookedTravel(models.Model):
	tripdetail = models.ForeignKey(TripDetail)

	flight_booked = models.BooleanField(default=False)
	price_paid_for_flight = models.PositiveIntegerField(default=0, blank=True)
	flight_ticket1 = models.FileField(upload_to='traveltriangle/flight', null=True, blank=True)
	flight_ticket2 = models.FileField(upload_to='traveltriangle/flight', null=True, blank=True)

	train_booked = models.BooleanField(default=False)
	price_paid_for_train = models.PositiveIntegerField(default=0, blank=True)
	train_ticket1 = models.FileField(upload_to='traveltriangle/train', null=True, blank=True)
	train_ticket2 = models.FileField(upload_to='traveltriangle/train', null=True, blank=True)
	pub_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)

	def __str__(self):
		return self.tripdetail.person_name

class BookedHotel(models.Model):
	tripdetail = models.ForeignKey(TripDetail, null=True)
	hotel = models.ForeignKey(Hotel, null=True, blank=True)
	room_type = models.CharField(max_length=225, null=True, blank=True)
	date = models.DateField(default=datetime.now,null=True, blank=True)
	hotel_nights = models.PositiveIntegerField(null=True,blank=True)
	room_numbers = models.PositiveIntegerField(null=True, blank=True)
	total_price = models.PositiveIntegerField(null=True, blank=True)
	price_paid = models.PositiveIntegerField(null=True, blank=True, default=0)
	pub_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)

	payment_reciept = models.FileField(upload_to='traveltriangle/payment_files', null=True, blank=True)
	booking_confirmation_received = models.BooleanField(default=False)

	def __str__(self):
		return self.tripdetail.person_name

class OtherBooking(models.Model):
	tripdetail = models.ForeignKey(TripDetail, null=True)
	heading = models.CharField(max_length=250,null=True, blank=True)
	total_price = models.PositiveIntegerField(null=True, blank=True)
	price_paid = models.PositiveIntegerField(null=True,blank=True)
	file = models.FileField(upload_to='traveltriangle/other', null=True, blank=True)
	pub_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)

	def __str__(self):
		return self.tripdetail.person_name

# Create your models her