from django.contrib import admin
from .models import Coords, Level, Pereval, Images

@admin.register(Coords)
class CoordsAdmin(admin.ModelAdmin):
    list_display = ('latitude', 'longitude', 'height')

@admin.register(Level)
class LevelAdmin(admin.ModelAdmin):
    list_display = ('winter', 'summer', 'autumn', 'spring')

@admin.register(Pereval)
class PerevalAdmin(admin.ModelAdmin):
    list_display = ('beauty_title', 'title', 'user', 'add_time', 'status')

@admin.register(Images)
class ImagesAdmin(admin.ModelAdmin):
    list_display = ('title', 'data_added', 'pereval')
