from django.db import models
from django.template.defaultfilters import slugify

from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import ResizeToFill

class StateDetail(models.Model):
    
    STATE_LIST = (
        ('Himachal Pradesh', 'Himachal Pradesh'),
        ('Uttarakhand', 'Uttarakhand'),
        ('Kerala', 'Kerala'),
        ('Rajasthan', 'Rajasthan'),
        ('Maharastra', 'Maharastra'),
        ('Jammu & Kashmir', 'Jammu & Kashmir'),
        ('West Bengal', 'West Bengal'),
        ('Sikkim', 'Sikkim'),
        ('Jammu & Kashmir', 'Jammu & Kashmir'),
        ('Meghalaya', 'Meghalaya'),
        ('Andaman & Nicobar', 'Andaman & Nicobar'),
        ('Karnataka', 'Karnataka'),
        ('Tamil Nadu', 'Tamil Nadu'),
        ('Andhra Pradesh', 'Andhra Pradesh'),
        ('Madhya Pradesh', 'Madhya Pradesh'),
        ('Uttar Pradesh', 'Uttar Pradesh'),
        ('Lakshadweep', 'Lakshadweep'),
    )
    state_name = models.CharField(max_length=128, choices=STATE_LIST,null=True)
    state_detail = models.TextField(max_length=100000, null=True)

    def __str__(self):
        return self.state_name
    

class PlaceDetail(models.Model):
    statedetail = models.ForeignKey(StateDetail)
    place_name = models.CharField(max_length=255, null=True)
    place_tagline = models.CharField(max_length=255, null=True, blank=True)
    place_detail = models.TextField(max_length=10000, null=True)
    main_img = ProcessedImageField(upload_to = 'places', null=True, blank=True, processors=[ResizeToFill(1200, 700)],
                                      format='JPEG',
                                      options={'quality': 70})

    credit_name = models.CharField(max_length=250, null=True, blank=True)
    licence_type = models.URLField(null=True,blank=True)
    credit_url = models.URLField(null=True, blank=True)


    slug = models.SlugField(null=True)

    def __str__(self):
        return self.place_name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.place_name)
        super(PlaceDetail, self).save(*args, **kwargs)

class PlaceToVisit(models.Model):
    placedetail = models.ForeignKey(PlaceDetail)
    attraction_name = models.CharField(max_length=250, null=True)
    attraction_detail = models.TextField(max_length=10000, null=True)
    attraction_img = ProcessedImageField(upload_to = 'places', null=True, blank=True, processors=[ResizeToFill(1200, 700)],
                                      format='JPEG',
                                      options={'quality': 70})
    credit_name = models.CharField(max_length=250, null=True, blank=True)
    licence_type = models.URLField(null=True,blank=True)
    credit_url = models.URLField(null=True, blank=True)

    attraction_url = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.attraction_name


class PlaceToEat(models.Model):
    placedetail = models.ForeignKey(PlaceDetail)
    name = models.CharField(max_length=250, null=True)
    detail = models.TextField(max_length=10000, null=True)
    place_img = ProcessedImageField(upload_to = 'places', null=True, blank=True, processors=[ResizeToFill(1200, 700)],
                                      format='JPEG',
                                      options={'quality': 70})
    credit_name = models.CharField(max_length=250, null=True, blank=True)
    licence_type = models.URLField(null=True,blank=True)
    credit_url = models.URLField(null=True, blank=True)


class ImpPoint(models.Model):
    placedetail = models.ForeignKey(PlaceDetail)
    heading = models.CharField(max_length=250, null=True)
    detail = models.TextField(max_length=10000, null=True)

class HowToReach(models.Model):
    placedetail = models.ForeignKey(PlaceDetail)

    CHOICE = (
        ('Railway', 'Railway'),
        ('Air', 'Air'),
        ('Road', 'Road'),
    )
    transpotation_type = models.CharField(max_length=128, choices=CHOICE,null=True)
    detail = models.TextField(max_length=100000, null=True)


class PlaceImage(models.Model):
    placedetail = models.ForeignKey(PlaceDetail)
    img = ProcessedImageField(upload_to = 'places', null=True, blank=True, processors=[ResizeToFill(1200, 700)],
                                      format='JPEG',
                                      options={'quality': 70})
    credit_name = models.CharField(max_length=250, null=True, blank=True)
    licence_type = models.URLField(null=True,blank=True)
    credit_url = models.URLField(null=True, blank=True)