from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages

def home(request):
    user_reg = UserCreationForm()
    user_auth = AuthenticationForm()

    if request.method == 'POST' and 'registration' in request.POST:
        user_reg = UserCreationForm(request.POST)
        if user_reg.is_valid():
            user_reg.save()
            messages.success(request, 'Success register')
            return redirect('home')

    elif request.method == 'POST' and 'authorization' in request.POST:
        user_auth = AuthenticationForm(request.POST)
        if user_auth.is_valid():
            return redirect('books')

    context = {'user_reg': user_reg, 'user_auth': user_auth}

    return render(request, 'user_forms/home.html', context=context)