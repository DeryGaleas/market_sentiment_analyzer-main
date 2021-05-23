from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django

# Create your views here.
def login(request):
    if request.user.is_authenticated:
        return redirect("home")
    if request.method == 'POST':

        post_form = request.POST

        user = authenticate(
            request,
            username=post_form.get("username"),
            password=post_form.get("password")
        )
        if user is not None:
            login_django(request, user)
            return redirect("home")
    return render(request, 'users/login.html')