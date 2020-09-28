from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from post.services import get_posts


class Site:
    domain = 'ertai.kz'


class BlogSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5
    protocol = 'https'

    def get_urls(self, site=None, **kwargs):
        site = Site()
        return super(BlogSitemap, self).get_urls(site=site, **kwargs)

    def location(self, item):
        return reverse('post_detail', args=(item.id, item.slug,))

    def items(self):
        return get_posts()

    def lastmod(self, obj):
        return obj.updated_at
