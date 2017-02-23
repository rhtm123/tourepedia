from django.conf.urls import patterns, url
from tours import views


urlpatterns = [
        url(r'^$', views.tour_packages, name='tour_packages'),
        url(r'^(?P<slug>[\w\-]+)/$', views.tour, name='tour'),
        url(r'^category/adventure/$', views.adventure, name='adventure'),
        url(r'^category/family/$', views.family, name='family'),
        url(r'^category/nature/$', views.nature, name='family'),
        url(r'^category/honeymoon/$', views.honeymoon, name='honeymoon'),
        url(r'^category/wildlife/$', views.wildlife, name='wildlife'),
        url(r'^category/hill-station/$', views.hill_station, name='hill_station'),
        url(r'^category/religious/$', views.religious, name='religious'),
        url(r'^category/beaches/$', views.beaches, name='beaches'),
       # url(r'^add_category/$', views.add_category, name= 'add_category')
]