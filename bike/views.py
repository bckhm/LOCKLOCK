from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.db import IntegrityError
from django.http import JsonResponse
from .models import User, Lot


# Renders index page
def index(request):
    user = request.user
    if user.is_authenticated:
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


# Returns info on a particular lot to JS
def check_lot(request, lotno):
    curr_lot = Lot.objects.get(number=lotno)
    return JsonResponse({
        "type": curr_lot.type,
        "number": curr_lot.number,
        "occupied": curr_lot.occupied_status})


# Changes occupied status in database to "No"
def unlock_lot(request, lotno):
    curr_lot = Lot.objects.get(id=lotno)
    curr_lot.occupied_status = "No"
    curr_lot.save()
    return JsonResponse({"Operation": "Unlock",
                         "Occupied": curr_lot.occupied_status})


# Changes occupied status in database to "Yes"
def lock_lot(request, lotno):
    curr_lot = Lot.objects.get(id=lotno)
    curr_lot.occupied_status = "Yes"
    curr_lot.save()
    return JsonResponse({"Operation": "Lock",
                         "Occupied": curr_lot.occupied_status})