from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("register", views.regisfunc, name="regispage"),
    path("login", views.loginfunc, name="loginpage"),
    path("logout", views.logoutfunc, name = 'logout'),
    path("getorder", views.getorderfunc, name = 'getorder'),
    path("getcart", views.getcartfunc, name = 'getcart'),
    path("placeorder", views.placeorderfunc, name = 'placeorder'),
    path("vieworder", views.vieworder, name= 'vieworder')

]
