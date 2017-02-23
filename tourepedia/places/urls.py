from django.conf.urls import patterns, url
from places import views

urlpatterns = [
		
        #url(r'^$', views.hotel_home, name='hotel_home'),
        url(r'^(?P<slug>[\w\-]+)/$', views.place, name='place'),
        url(r'^(?P<slug>[\w\-]+)/tour-packages/$', views.tourforplace,  name='tourforplace'),
       # url(r'^add_category/$', views.add_category, name= 'add_category')
]