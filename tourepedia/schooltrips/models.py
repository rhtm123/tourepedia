from django.db import models

from places.models import StateDetail, PlaceDetail
from django.template.defaultfilters import slugify

from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import ResizeToFill

from general.models import  Inclusion, Exclusion, Term

# Create your models here.

class SchoolTourDetail(models.Model):
	statedetail = models.ForeignKey(StateDetail,null=True)
	placedetail = models.ForeignKey(PlaceDetail,null=True)
	tour_name = models.CharField(max_length=250, null=True)
	tour_price = models.IntegerField(null=True)
	number_days = models.CharField(max_length=250, null=True)

	#tour_tagline = models.CharField(max_length=250, null=True)
	tour_detail = models.TextField(max_length=10000,null=True)

	main_img = ProcessedImageField(upload_to = 'schooltrips', null=True, blank=True, processors=[ResizeToFill(1200, 600)],
                                      format='JPEG',
                                      options={'quality': 70})

	slug = models.SlugField(null=True, max_length=250)

	inclusion_type = models.ForeignKey(Inclusion, null=True)
	exclusion_type = models.ForeignKey(Exclusion, null=True)

	term_type = models.ForeignKey(Term, null=True, blank=True)

	def save(self, *args, **kwargs):
		self.slug = slugify(self.tour_name)
		super(SchoolTourDetail, self).save(*args, **kwargs)

	def __str__(self):
		return self.tour_name



class SchoolTourCategory(models.Model):
	tourdetail = models.ForeignKey(SchoolTourDetail)
	CAT = (
		('Nature', 'Nature'),
		('Adventure', 'Adventure'),
		('Hill Station', 'Hill Station'),
		('Religious & Spiritual','religious & Spiritual'),
		('Beaches', 'Beaches'),
		('Wildlife', 'Wildlife'),
	)
	category = models.CharField(max_length=128, choices=CAT, null=True)


class SchoolTourItinerary(models.Model):
    tourdetail = models.ForeignKey(SchoolTourDetail)
    tour_day = models.IntegerField(null=True)
    tour_itinerary = models.TextField(max_length=10000, null=True)
    tour_stay = models.CharField(max_length=250,null=True)

class SchoolTourImage(models.Model):
    tourdetail = models.ForeignKey(SchoolTourDetail)
    img = ProcessedImageField(upload_to = 'schooltrips', null=True, blank=True, processors=[ResizeToFill(1200, 600)],
                                      format='JPEG',
                                      options={'quality': 70})

# Create your models here.
