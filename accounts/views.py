# accounts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Avtomatik login qilsin
            return redirect('home.html')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})
