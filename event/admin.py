from django.contrib import admin

from event import models


@admin.register(models.Event)
class EventAdmin(admin.ModelAdmin):

    list_display = ['id', 'shop', 'is_enabled', 'description']
    raw_id_fields = ['shop']


