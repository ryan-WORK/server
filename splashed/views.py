from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect


def app_index(request):
    return render(request, 'splashed/splashed.html', {})


def app_mar(request):
    return render(request, 'splashed/ar1.html', {})


def app_dad(request):
    return render(request, 'splashed/ar2.html', {})


def app_mom(request):
    return render(request, 'splashed/ar3.html', {})
# def signup(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             raw_password = form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=raw_password)
#             login(request, user)
#             return redirect('home')
#     else:
#         form = UserCreationForm()
#     return render(request, 'splashed/signup.html', {'form': form})
