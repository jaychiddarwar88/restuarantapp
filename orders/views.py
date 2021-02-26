from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import subs, pasta, salads, dinplatter, toppings, regularpizza, silicanpizza, cart, orders
import re
from django.db.models import Max
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

apikey ='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'
# Create your views here.
def index(request):
    if not request.user.is_authenticated :
        return render(request , 'orders/loginpage.html')
    else :
        context = {
            "subs" : subs.objects.all(),
            "pasta" : pasta.objects.all(),
            "salads" : salads.objects.all(),
            "dinplatter" : salads.objects.all(),
            "toppings" : toppings.objects.all(),
            "regularpizza" : regularpizza.objects.all(),
            "silicanpizza" : silicanpizza.objects.all()
        }
        return render(request, 'orders/mainpage.html', context)

def regisfunc(request):
    if request.method == 'POST':
        username = request.POST['regname']
        email = request.POST['regemail']
        password = request.POST['regpassword']
        user = User.objects.create_user(username = username, password = password, email = email)
        user.save()
        print("user created successfully")
        return render(request, 'orders/loginpage.html')
    else :
        return render(request, 'orders/regispage.html')

def loginfunc(request):
    username = request.POST['loginuser']
    password = request.POST['loginpassword']
    user = authenticate(request,username = username, password = password)
    if user is not None:
        login(request, user)
        return index(request)
    else:
        print('fail')
        return render(request, "orders/loginpage.html")

def logoutfunc(request):
    logout(request)
    print("logout successful")
    return render(request, 'orders/loginpage.html')

def getorderfunc(request):
    username = request.user.username
    category = request.POST['category']
    ordername = request.POST['order']
    cart.objects.create(user = username, category= category, ordername = ordername, price = float(re.findall("\d+\.\d+", ordername)[0]))
    return HttpResponse("success")

def getcartfunc(request):
    username = request.user.username
    dets = cart.objects.filter(user = username)
    total = 0
    for i in dets.values('price'):
        total = total + i['price']
    context = {
        "details" : dets,
        "total" : str(total)
    }
    return render(request, 'orders/cartpage.html', context)

def placeorderfunc(request):
    username = request.user.username
    dets = cart.objects.filter(user = username)
    max = orders.objects.all().aggregate(Max('orderid'))
    max = max['orderid__max']
    max = max + 1
    for i in dets.values():
        orders.objects.create(orderid = max, user = username, category = i['category'], ordername = i['ordername'], price = i['price'])
    dets.delete()

    email = User.objects.filter(username = username).values('email')[0]['email']

    message = Mail(
        from_email='jjsschiddarwar@gmail.com',
        to_emails=email,
        subject='Pizza Restaurant Order',
        html_content='<strong>Your order is confirmed, check order at website at my order!!</strong>'
        + '<p> click to see orders : <a href="http://127.0.0.1:8000/vieworder">orders</a></p>')
    try:
        sg = SendGridAPIClient(apikey)
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print( e.message)

    return index(request)

def vieworder(request):
    username = request.user.username
    
    dets = orders.objects.filter(user = username)
    total = 0
    for i in dets.values('price'):
        total = total + i['price']


    context = {
        "details" : dets,
        "total" : str(total)
    }

    return render(request, 'orders/vieworders.html', context)