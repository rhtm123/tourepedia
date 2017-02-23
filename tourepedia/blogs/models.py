
from datetime import datetime
from django.db import models
from django.template.defaultfilters import slugify

from django.core.urlresolvers import reverse

from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import ResizeToFill

from places.models import StateDetail, PlaceDetail


class Tag(models.Model):
    tag_name= models.CharField(max_length= 128, null=True, blank=True)
    def __str__(self):
        return self.tag_name


class Title(models.Model):
    header = models.CharField(max_length=255, null=True, unique=True)
    head_img = ProcessedImageField(upload_to = 'blogs', null=True, blank=True, processors=[ResizeToFill(1200, 700)],
                                      format='JPEG',
                                      options={'quality': 70})

    pub_date= models.DateTimeField(default=datetime.now, blank=True)
    expected_time = models.IntegerField(blank=True, null=True)
    publisher = models.CharField(max_length=255, null=True, blank=True)
    likes = models.IntegerField(default=0, blank=True)
    slug = models.SlugField(null=True)    
    views = models.IntegerField(default=0)

    BLOG_TYPE = (
        ('inspired', 'Be Inspired'),
        ('photoblog', 'Photo Blog'),
        ('tips', 'Travel Tips'),
        ('stories', 'Travel Stories'),
    )
    blog_type = models.CharField(max_length=128, choices=BLOG_TYPE,null=True)
    content = models.TextField(max_length=100000, null=True)

    def __str__(self):
        return self.state_name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.header)
        super(Title, self).save(*args, **kwargs)

    def __str__(self):
        return self.header

    def get_absolute_url(self):
        return reverse('blogs.views.detail', args=(self.slug,))


class Detail(models.Model):
    title = models.ForeignKey(Title)
    heading = models.CharField(max_length=255, null=True, blank=True)
    content = models.TextField(max_length=10024, null=True)
    quote = models.TextField(max_length=1024, null=True, blank=True)

    img_content = ProcessedImageField(upload_to='blogs', null=True, blank=True, format='JPEG', options={'quality': 20})
    #fig_caption = models.CharField(max_length=255, null=True, blank=True)
    img_credit_name = models.CharField(max_length=255, null=True, blank=True)
    img_credit_link = models.URLField(null=True, blank=True)
    license_type = models.URLField(null=True, blank=True)
   # img_content = models.ImageField(upload_to= 'blogs', null=True, blank=True)
    

    def __str__(self):
        return self.heading

class PlaceDescribedInBlog(models.Model):
    title = models.ForeignKey(Title, null=True)
    #statedetail = models.ForeignKey(StateDetail,null=True)
    placedetail = models.ForeignKey(PlaceDetail,null=True)


class TagForBlog(models.Model):
    title = models.ForeignKey(Title, null=True)
    tag = models.ForeignKey(Tag, null=True, blank=True)
