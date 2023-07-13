from django.contrib import admin
from models_relations.models import Album, Song

# Register your models here.
@admin.register(Album)
class models_relations(admin.ModelAdmin):
    pass

@admin.register(Song)
class models_relations(admin.ModelAdmin):
    pass