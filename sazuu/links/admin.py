from django.contrib import admin
from .models import Link

class LinkAdmin(admin.ModelAdmin):
    list_display = ('service', 'sort_order')

admin.site.register(Link, LinkAdmin)