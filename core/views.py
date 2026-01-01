
from django.http import HttpResponse
from django.shortcuts import render,redirect

def home(request):
    if 'username' not in request.session:
        return redirect("login")
    return render(request, "home.html", {"username": request.session['username']})
