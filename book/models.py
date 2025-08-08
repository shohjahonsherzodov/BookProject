from django.db import models
from django.contrib.auth.models import User

# 1. Kategoriya modeli
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# 2. Muallif modeli
class Author(models.Model):
    full_name = models.CharField(max_length=200)
    bio = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='authors/', blank=True, null=True)

    def __str__(self):
        return self.full_name


# 3. Kitob modeli
class Book(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='books')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='books')
    image = models.ImageField(upload_to='books/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


# 4. Izoh (kommentariya) modeli
class Comment(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Izoh: {self.user.username} -> {self.book.title}"


# 5. Reyting modeli
class Rating(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='ratings')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField()  # 1 dan 5 gacha

    def __str__(self):
        return f"{self.rating}⭐ by {self.user.username} for {self.book.title}"


# 6. Yangiliklar (Feed) modeli
class Feed(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='feeds/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
