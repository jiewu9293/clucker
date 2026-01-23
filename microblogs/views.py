from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import SignUpForm
from .models import User

# Create your views here.
def home(request):
    return render(request,'home.html')
def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            User.objects.create_user(
                form.cleaned_data.get('username'),
                email = form.cleaned_data.get('email'),
                first_name = form.cleaned_data.get('first_name'),
                last_name = form.cleaned_data.get('last_name'),
                bio = form.cleaned_data.get('bio'),
                password = form.cleaned_data.get('new_password')
            )
            return redirect('feed')

    else:
        form = SignUpForm()
    return render(request,'sign_up.html',{'form':form})

def feed(request):
    return render(request,'feed.html')
