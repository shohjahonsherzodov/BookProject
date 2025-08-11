from django.shortcuts import render, get_object_or_404, redirect
from .models import Book
from .forms import BookForm

def home(request):
    books = Book.objects.all()
    return render(request, 'book/home.html', {'books': books})

def book_list(request):
    books = Book.objects.all().order_by('-created_at')
    return render(request, 'book/book_list.html', {'books': books})

def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'book/book_detail.html', {'book': book})

def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            book = form.save(commit=False)
            book.user = request.user  # foydalanuvchini bog‘lash
            book.save()
            return redirect('book_detail', pk=book.pk)
    else:
        form = BookForm()
    return render(request, 'book/book_form.html', {'form': form})

def update_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book:book_detail', pk=pk)
    else:
        form = BookForm(instance=book)
    return render(request, 'book/form.html', {'form': form})

def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book:book_list')
    return render(request, 'book/book_confirm_delete.html', {'book': book})
