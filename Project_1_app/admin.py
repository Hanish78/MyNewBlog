from django.contrib import admin
from .models import BlogContent

# Register your models here.
@admin.register(BlogContent)
class BlogContent(admin.ModelAdmin):
    pass

