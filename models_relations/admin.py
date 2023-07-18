from django.contrib import admin
from models_relations.models import Album, Song, Author, Book, Vehicle, Car

# Register your models here.
@admin.register(Album)
class models_relations(admin.ModelAdmin):
    pass

admin.site.register(Song)
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Vehicle)
admin.site.register(Car)

