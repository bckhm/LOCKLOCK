from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("status/<int:lotno>", views.check_lot, name="check_lot"),
    path("unlock/<int:lotno>", views.unlock_lot, name="unlock"),
    path("lock/<int:lotno>", views.lock_lot, name="lock")
]