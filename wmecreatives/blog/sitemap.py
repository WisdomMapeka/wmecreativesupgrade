from django.contrib.sitemaps import Sitemap
from .models import Articles, Categories
from django.contrib import sitemaps
from django.urls import reverse

class ArticleSitemap(Sitemap):
	def items(self):
		return Articles.objects.all()
		
	def lastmod(self, obj):
		return obj.date_updated

class CategoriesSitemap(Sitemap):
	def items(self):
		return Categories.objects.all()
		
	def lastmod(self, obj):
		return obj.date_updated
	
class StaticViewSitemap(sitemaps.Sitemap):
    # priority = 0.5
    # changefreq = "daily"

    def items(self):
        return ["contacts"]

    def location(self, item):
        return reverse(item)
