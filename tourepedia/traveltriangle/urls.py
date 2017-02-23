from django.conf.urls import patterns, url
from traveltriangle import views

urlpatterns = [
        url(r'^$', views.traveltriangle_index, name='traveltriangle_index'),
        url(r'in-progress/$', views.inprogress, name='inprogress'),
        url(r'booked/$', views.booked, name='booked'),
        url(r'cancelled/$', views.cancelled, name='cancelled'),

        url(r'quote/$', views.quote, name='quote'),
        url(r'quote/search/', views.quote_search, name='quote_search'),

        url(r'quote/(?P<pk>\d+)/$', views.quote_view, name='quote_view'),
        url(r'quote/(?P<pk>\d+)/info-edit/$', views.info_edit, name='info_edit'),
        url(r'quote/(?P<pk>\d+)/imp-edit/$', views.imp_edit, name='imp_edit'),
       # url(r'quote/(?P<pk>\d+)/itinerary-edit/$', views.itinerary_edit, name='itinerary_edit'),
       # url(r'^add_category/$', views.add_category, name= 'add_category')

       url(r'itinerary/$' , views.itinerary_main, name= 'itinerary_main'),

       url(r'itinerary/search/', views.itinerary_search, name='itinerary_search'),
       url(r'itinerary/(?P<slug>[\w-]+)/$' , views.itinerary , name='itinerary'),
]
