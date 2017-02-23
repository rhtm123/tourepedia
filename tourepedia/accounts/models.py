from django.db import models
from django.contrib.auth.models import User

from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import ResizeToFill

class UserProfile(models.Model):
    user = models.OneToOneField(User)

    #picture = models.ImageField(upload_to='accounts', blank=True)

    picture = ProcessedImageField(upload_to = 'accounts', null=True, blank=True,processors=[ResizeToFill(400,400)],
                                      format='JPEG',
                                      options={'quality': 70})

    def __str__(self):
        return self.user.username

'''
class UserDetail(models.Model):
	user = models.OneToOneField(User)
	userprofile = models.ForeignKey(UserProfile)
	#address = models.CharField(max_length = 1024, null=True)
	#about = models.TextField(max_length= 100000, null=True)
	
'''