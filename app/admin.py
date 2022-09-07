from django.contrib import admin

from app.models import Server, ServerDetail


@admin.register(Server)
class ServerAdmin(admin.ModelAdmin):
    list_display = ('id', 'plan_id', 'ram', 'hdd')


@admin.register(ServerDetail)
class ServerDetailAdmin(admin.ModelAdmin):
    list_display = ('id', 'server', 'city', 'country')
