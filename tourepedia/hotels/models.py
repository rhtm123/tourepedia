from django.db import models
from datetime import datetime

from django.template.defaultfilters import slugify

from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import ResizeToFill

from places.models import PlaceDetail


class FacilityType(models.Model):
	facility_type = models.CharField(max_length=255)

	def __str__(self):
		return self.facility_type


class Facility(models.Model):
	facilitytype = models.ForeignKey(FacilityType)
	facility = models.CharField(max_length=255)



class Hotel(models.Model):
	placedetail = models.ForeignKey(PlaceDetail,null=True)
	hotel_name = models.CharField(max_length=240, blank=True)
	city = models.CharField(max_length=240, null=True,blank=True)
	concerned_person = models.CharField(max_length=250, null=True, blank=True)
	mobile_number1 = models.CharField(max_length=250, null=True, blank=True)
	mobile_number2 = models.CharField(max_length=250, null=True, blank=True)
	email_id = models.CharField(max_length=250,null=True, blank=True)


	starting_price = models.IntegerField(null=True)
	
	hotel_address = models.CharField(max_length=480, blank=True)

	main_img = ProcessedImageField(upload_to = 'hotels', null=True, blank=True, processors=[ResizeToFill(1200, 700)],
                                      format='JPEG',
                                      options={'quality': 70}) 

	about_hotel = models.TextField(max_length=10000, blank=True)
	map_link = models.URLField(blank=True)

	star_rating = models.IntegerField(blank=True)

	slug = models.SlugField(max_length=240,null=True)

	facility_type = models.ForeignKey(FacilityType, null=True)

	def __str__(self):
		return self.hotel_name

	def save(self, *args, **kwargs):
		self.slug = slugify(self.hotel_name)
		super(Hotel, self).save(*args, **kwargs)





class HotelRoomImg(models.Model):
	hotel = models.ForeignKey(Hotel)
	room_img = ProcessedImageField(upload_to = 'hotels', null=True, blank=True, processors=[ResizeToFill(1200, 700)],
                                      format='JPEG',
                                      options={'quality': 70})  

class HotelViewImg(models.Model):
	hotel = models.ForeignKey(Hotel)
	view_img = ProcessedImageField(upload_to = 'hotels', null=True, blank=True, processors=[ResizeToFill(1200, 700)],
                                      format='JPEG',
                                      options={'quality': 70})

class HotelSeason(models.Model):
	hotel = models.ForeignKey(Hotel)
	start = models.DateField(null=True, blank=True)
	end = models.DateField(null=True, blank=True)


class HotelPrice(models.Model):
	hotel = models.ForeignKey(Hotel, null=True)
	room_type = models.CharField(max_length=128,null=True)
	price = models.IntegerField(null=True)
	extra_person_cost = models.IntegerField(null=True, blank=True)
	season_price = models.IntegerField(null=True, blank=True)
	season_extra_person_cost = models.IntegerField(null=True, blank=True)
# Create your models here.
