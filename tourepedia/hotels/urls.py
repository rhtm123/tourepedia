from django.conf.urls import patterns, url
from hotels import views

urlpatterns = [
        url(r'^$', views.hotel_home, name='hotel_home'),
        url(r'^(?P<slug>[\w-]+)/$', views.hotel_detail, name='hotel_detail'),
        url(r'^search/hotel-search/$', views.hotel_search, name='hotel_search'),
       # url(r'^add_category/$', views.add_category, name= 'add_category')
]
