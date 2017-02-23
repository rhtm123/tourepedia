from django.conf.urls import patterns, url
from blogs import views

urlpatterns = [
        url(r'^$', views.index, name='index'),
        url(r'^(?P<slug>[\w-]+)/$', views.detail, name='detail'),
        url(r'category/be-inspired/$', views.inspired_index, name='inspired_index'),
        url(r'category/photoblog/$', views.photoblog_index, name='photoblog_index'),
        url(r'category/travel-tips/$', views.traveltip_index, name='treveltip_index'),
        url(r'category/travel-tales/$', views.tales_index, name='tales_index'),
       # url(r'^add_category/$', views.add_category, name= 'add_category')
]
