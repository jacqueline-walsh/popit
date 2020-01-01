from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from accounts.forms import UserLoginForm

# log in page for user
def login(request):
    if request.user.is_authenticated:
        return redirect(reverse('index'))
    if request.method == 'POST':
        login_form = UserLoginForm(request.POST)

        if login_form.is_valid():
            user = auth.authenticate(
                username=request.POST['username'],
                password=request.POST['password'])

            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have successfully logged in!")
                return redirect(reverse('index'))

            else:
                login_form.add_error(None, "Your username or password is incorrect!")
    else:
        login_form = UserLoginForm()

    context =   {"login_form" : login_form}
    return render(request, 'accounts/login.html', context)

# logout page for user
@login_required
def logout(request):
    auth.logout(request)
    messages.success(request, "You have successfully been logged out!")
    return redirect(reverse('index'))