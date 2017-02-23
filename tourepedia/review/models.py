from datetime import datetime

from django.db import models
from django.contrib.auth.models import User

from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import ResizeToFill

from tours.models import TourDetail
from schooltrips.models import SchoolTourDetail
from hotels.models import Hotel

from accounts.models import UserProfile

class ReviewForTours(models.Model):
	user = models.ForeignKey(User,null=True)

	user_image = ProcessedImageField(upload_to = 'review', null=True, blank=True,processors=[ResizeToFill(400,400)],
                                      format='JPEG',
                                      options={'quality': 70})

	tourdetail = models.ForeignKey(TourDetail,null=True)
    
	review_text = models.TextField(max_length=1000, null=True)
	pub_date= models.DateTimeField(default=datetime.now, blank=True)

	def __str__(self):
		return self.review_text

class ReviewForSchoolTrip(models.Model):
	user = models.ForeignKey(User)
	school_tour = models.ForeignKey(SchoolTourDetail, null=True)

	user_image = ProcessedImageField(upload_to = 'review', null=True, blank=True,processors=[ResizeToFill(400,400)],
                                      format='JPEG',
                                      options={'quality': 70})

	review_text = models.TextField(max_length=1000, null=True)
	school_name = models.CharField(max_length=255, null=True)
	pub_date= models.DateTimeField(default=datetime.now, blank=True)

	def __str__(self):
		return self.school_name


class ReviewForHotel(models.Model):
	user = models.ForeignKey(User)
	hotel = models.ForeignKey(Hotel)
	review_text = models.TextField(max_length=1000,null=True)
	pub_date= models.DateTimeField(default=datetime.now, blank=True)

# Create your models here.
