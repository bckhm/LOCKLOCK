from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.db import IntegrityError
from django.http import JsonResponse
from .models import User


# Renders index page
def index(request):
    if request.user.is_authenticated:
        return render(request, 'bike/index.html')

    else:
        return HttpResponseRedirect(reverse('login'))

# Login verification using user's email and password
def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        email = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(request, username=email, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "bike/login.html", {
                "message": "Invalid email and/or password."
            })
    else:
        return render(request, "bike/login.html")


# Logout, leads to index view
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


# Registration
def register(request):
    if request.method == "POST":
        email = request.POST["email"]
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "bike/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username=email,
                                            email=email,
                                            password=password,
                                            first_name=firstname,
                                            last_name=lastname)
            user.save()
        except IntegrityError as e:
            print(e)
            return render(request, "bike/register.html", {
                "message": "Email address already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "bike/register.html")