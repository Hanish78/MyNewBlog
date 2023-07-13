from django.contrib import admin
from .models import BlogContent

# Register your models here.
@admin.register(BlogContent)
class BlogContent(admin.ModelAdmin):
    search_fields = ['title']
    list_filter = ['description']
    list_display = ['title','author']

