from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages
def signup(request):
    error = ""
    if 'username' in request.session:
        return redirect("home")
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        if password != confirm_password:
             messages.error(request, "Passwords do not match")
        
        else:
            user = User.objects.create(
                username=username,
                password=password
            )
            # Auto-login after signup
            request.session['username'] = user.username
            
            return redirect("home")

    return render(request, "signup.html", {"error": error})



def login(request):
    error = ""
    if 'username' in request.session:
        return redirect("home")
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        try:
            user = User.objects.get(username=username)
            if user.password == password:
                # ✅ Save username in session
                request.session['username'] = user.username
                
                return redirect("home")
            else:
                error = "Incorrect password"
        except User.DoesNotExist:
            error = "User does not exist"

    return render(request, "login.html", {"error": error})

def logout(request):
    # Remove username from session
    request.session.flush()
    return redirect("login")
