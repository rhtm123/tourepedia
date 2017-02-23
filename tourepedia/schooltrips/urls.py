from django.conf.urls import patterns, url
from schooltrips import views

urlpatterns = [
        url(r'^$', views.school_home, name='school_home'),
        url(r'^(?P<slug>[\w\-]+)/$', views.school_trip, name='school_trip'),
       # url(r'^add_category/$', views.add_category, name= 'add_category')
]