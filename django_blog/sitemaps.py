from django.contrib.sitemaps import Sitemap
from site_page.models import Blog
from django.utils import timezone

class BlogSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):
        return Blog.objects.filter(publish=True)

    def lastmod(self, obj):
        return timezone.now()