from django.contrib import admin
from .models import Team, Contactus
from django.utils.html import format_html

# Register your models here.

class TeamAdmin(admin.ModelAdmin):
    def thumbnails(self, object):
        return format_html('<img src="{}" width="50px" style="border-radius:50px;" />'.format(object.image.url))

    thumbnails.short_description = 'photo'

    list_display = ('id', 'thumbnails', 'firstName', 'designation', 'date')
    list_display_links = ('id', 'firstName')
    search_fields = ('firstName', 'designation')
    list_filter = ('designation',)

admin.site.register(Team, TeamAdmin)


class AdminContactus(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'phone')
    list_display_links = ('name', 'email')
    search_fields = ('name', 'email')
admin.site.register(Contactus, AdminContactus)