from django.contrib.sitemaps import Sitemap

from blogs.models import Title

class BlogSitemap(Sitemap):
	changefreq = "weekly"
	priority = 0.5

	def items(self):
		return Title.objects.all()

	def lastmod(self, obj):
		return obj.pub_date