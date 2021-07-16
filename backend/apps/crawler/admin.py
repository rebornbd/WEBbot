from django.contrib import admin

from .models import Site, RelatedSite

class SiteAdmin(admin.ModelAdmin):
    fields          = ['url', 'title', 'content']
    list_display    = ('url', 'title', 'content', 'update')
    search_fields   = ['url', 'title', 'content']
    list_filter     = ['url']
    pass

class RelatedSiteAdmin(admin.ModelAdmin):
    fields          = ['url', 'title', 'content', 'site']
    list_display    = ('url', 'title', 'content', 'site', 'update')
    search_fields   = ['url', 'title', 'content', 'site']
    list_filter     = ['url']


admin.site.register(Site, SiteAdmin)
admin.site.register(RelatedSite, RelatedSiteAdmin)
