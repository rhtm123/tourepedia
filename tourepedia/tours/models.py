from django.db import models
from datetime import datetime
from django.template.defaultfilters import slugify

from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import ResizeToFill

from places.models import StateDetail, PlaceDetail
from general.models import Inclusion, Exclusion, Term

from hotels.models import Hotel


# Create your models here.

class TourDetail(models.Model):
	placedetail = models.ForeignKey(PlaceDetail,null=True)
	tour_name = models.CharField(max_length=250, null=True)
	tour_price = models.IntegerField(null=True)
	number_days = models.IntegerField(null=True)
	tour_tagline = models.CharField(max_length=250, null=True)
	tour_detail = models.TextField(max_length=10000,null=True)
	pub_date = models.DateTimeField(default=datetime.now, null=True, blank=True)
	main_img = ProcessedImageField(upload_to = 'tours', null=True, blank=True, processors=[ResizeToFill(1200, 700)],
                                      format='JPEG',
                                      options={'quality': 70})
	credit_name = models.CharField(max_length=250, null=True, blank=True)
	licence_type = models.URLField(null=True,blank=True)
	credit_url = models.URLField(null=True, blank=True)


	view = models.IntegerField(default=0, null=True)

	inclusion_type = models.ForeignKey(Inclusion, null=True, blank=True)
	exclusion_type = models.ForeignKey(Exclusion, null=True, blank=True)

	term_type = models.ForeignKey(Term, null=True, blank=True)

	slug = models.SlugField(null=True)

	def save(self, *args, **kwargs):
		self.slug = slugify(self.tour_name)
		super(TourDetail, self).save(*args, **kwargs)

	def __str__(self):
		return self.tour_name



class TourCategory(models.Model):
	tourdetail = models.ForeignKey(TourDetail)
	CAT = (
		('Nature', 'Nature'),
		('Romantic', 'Romantic'),
		('Family', 'Family'),
		('Hill-Station', 'Hill-Station'),
		('Adventure', 'Adventure'),
		('Religious','religious'),
		('Beaches', 'Beaches'),
		('Wildlife', 'Wildlife'),
	)
	category = models.CharField(max_length=128, choices=CAT, null=True)

class TourItinerary(models.Model):
    tourdetail = models.ForeignKey(TourDetail)
    tour_day = models.PositiveIntegerField(null=True)
    tour_day_title = models.CharField(null=True, max_length=255)
    tour_itinerary = models.TextField(max_length=10000, null=True)
    #tour_stay = models.CharField(max_length=250,null=True, blank=True)
    tour_stays = models.ForeignKey(Hotel, null=True, blank=True, )

    	
class TourImage(models.Model):
    tourdetail = models.ForeignKey(TourDetail)
    img = ProcessedImageField(upload_to = 'tours', null=True, blank=True, processors=[ResizeToFill(1200, 600)],
                                      format='JPEG',
                                      options={'quality': 70})
    credit_name = models.CharField(max_length=250, null=True, blank=True)
    licence_type = models.URLField(null=True,blank=True)
    credit_url = models.URLField(null=True, blank=True)

class ImportantPoint(models.Model):
	tourdetail = models.ForeignKey(TourDetail, null=True)
	title = models.CharField(max_length=255, null=True, blank=True)
	imp_points = models.TextField(null=True, blank=True)

class PlacesInclude(models.Model):
	tourdetail = models.ForeignKey(TourDetail, null=True)
	placedetail = models.ForeignKey(PlaceDetail,null=True)
