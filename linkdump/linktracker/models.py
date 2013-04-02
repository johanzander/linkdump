from django.db import models
from django.contrib import admin

class Link (models.Model):

    link_description = models.CharField(max_length=200)
    link_url = models.CharField(max_length=200)

    def __str__(self):
        return self.link_description


class LinkAdmin(admin.ModelAdmin):
    pass

admin.site.register(Link, LinkAdmin)
