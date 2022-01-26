from atexit import register
from sqlite3 import register_adapter
from django.contrib import admin

from . models import Post, Author, Tag

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_filter = ("author", "tag", "date")
    list_display = ("title", "author" ,"date")
    prepopulated_fields = {"slug": ("title",)}

class AuthorAdmin(admin.ModelAdmin):
    list_display = ("full_name", "email")



admin.site.register(Post, PostAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Tag)