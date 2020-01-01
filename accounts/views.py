from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages

# log in page for user
def login(request):
    return render(request, 'accounts/login.html')

# logout page for user
def logout(request):
    auth.logout(request)
    messages.success(request, "You have successfully been logged out!")
    return redirect(reverse('index'))