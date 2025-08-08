# book/admin.py
from django.contrib import admin
from .models import Book, Author, Category, Comment, Rating, Feed

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Rating)
admin.site.register(Feed)
