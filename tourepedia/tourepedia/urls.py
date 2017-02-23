"""tourepedia URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap

from tours import views

from blogs.sitemap import BlogSitemap

sitemaps = {
    'blogs':BlogSitemap
}


def i18n_javascript(request):
  return admin.site.i18n_javascript(request)




urlpatterns = [
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps},
    name='django.contrib.sitemaps.views.sitemap'),
    url(r'^robots.txt',include('robots.urls')),

    
    url(r'^summernote/', include('django_summernote.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^blog/', include('blogs.urls')),

    url(r'^$', views.home, name='home'),
    url(r'^search/$', views.main_search, name='main_search'),

    url(r'^tour-packages/', include('tours.urls')),
    url(r'^school-trips/', include('schooltrips.urls')),

    url(r'^accounts/', include('accounts.urls')),
    url(r'^hotels/', include('hotels.urls')),
    url(r'^places/', include('places.urls')),

    url(r'^travel-triangle/' , include('traveltriangle.urls')),

    url(r'^my_admin/jsi18n', i18n_javascript),
    
    #url(r'^googleaf3327db24afef20', TemplateView.as_view(template_name='googleaf3327db24afef20.html'), name='google-analytics'),

] 


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
