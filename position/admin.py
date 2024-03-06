from django.contrib import admin

from position.models import Position


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = [
        'position_id','position_name']
