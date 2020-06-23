from django.contrib import admin

from app.models import Server


@admin.register(Server)
class AddS3FileAdmin(admin.ModelAdmin):
    list_display = ('id', 'plan_id', 'ram', 'hdd')
