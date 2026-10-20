
from django.contrib import admin
from .models import Sensor


@admin.register(Sensor)
class SensorAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'sensor_type',
        'location',
        'is_active',
        'created_at',
    )
    list_filter = ('sensor_type', 'is_active')
    search_fields = ('name', 'location')
