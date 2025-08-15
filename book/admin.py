# book/admin.py
from django.contrib import admin
from .models import Book, Author, Category, Comment, Rating, Feed

class BookAdmin(admin.ModelAdmin):
    search_fields = ("title", )
admin.site.register(Book, BookAdmin)
admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Rating)
admin.site.register(Feed)
