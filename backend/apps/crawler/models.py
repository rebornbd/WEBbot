from django.db import models


class Site(models.Model):
    url     = models.CharField(max_length=200, blank=True, null=True)
    title   = models.TextField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    update  = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = " site"
        verbose_name_plural = " sites"
    
    def __str__(self):
        return self.title[:20]


class RelatedSite(models.Model):
    site    = models.ForeignKey(Site, related_name='relatedsites', on_delete=models.CASCADE)
    url     = models.CharField(max_length=200, blank=True, null=True)
    title   = models.TextField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    update  = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = " related-site"
        verbose_name_plural = " related-sites"

    def __str__(self):
        return self.title[:20]
