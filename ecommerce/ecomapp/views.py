from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.conf import settings
from .models import Product,Contact,Orders,OrderUpdate
from math import ceil
import json
from django.views.decorators.csrf import  csrf_exempt

# Create your views here.
def home(request):
    current_user = request.user
    print(current_user)
    allProds = []
    catprods = Product.objects.values('category','id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod= Product.objects.filter(category=cat)
        n=len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])

    params= {'allProds':allProds}
    return render(request,'index.html',params)




def about(request):
    return render(request, 'about.html')



def contactus(request):
    if request.method=="POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
        messages.success(request,"Contact Form is Submitted")
  
    return render(request, 'contactus.html')



def tracker(request):
    if request.method=="POST":
        orderId = request.POST.get('orderId', '')
        email = request.POST.get('email', '')
        try:
            order = Orders.objects.filter(order_id=orderId, email=email)
            if len(order)>0:
                update = OrderUpdate.objects.filter(order_id=orderId)
                updates = []
                for item in update:
                    updates.append({'text': item.update_desc, 'time': item.timestamp})
                    response = json.dumps([updates, order[0].items_json], default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('{}')
        except Exception as e:
            return HttpResponse('{}')

    return render(request, 'tracker.html')




def productView(request, myid):
    # Fetch the product using the id
    product = Product.objects.filter(id=myid)


    return render(request, 'prodView.html', {'product':product[0]})



    

def checkout(request):
    if request.method=="POST":

        items_json = request.POST.get('itemsJson', '')
        name = request.POST.get('name', '')
        amount = request.POST.get('amt')
        email = request.POST.get('email', '')
        address1 = request.POST.get('address1', '')
        address2 = request.POST.get('address2','')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zip_code', '')
        phone = request.POST.get('phone', '')
         

        Order = Orders(items_json=items_json,name=name,amount=amount, email=email, address1=address1,address2=address2,city=city,state=state,zip_code=zip_code,phone=phone)
        print(amount)
        Order.save()
        update = OrderUpdate(order_id=Order.order_id,update_desc="the order has been placed")
        update.save()
        thank = True
        id = Order.order_id
        return render(request, 'checkout.html', {'thank': thank, 'id': id})

    return render(request, 'checkout.html')


def handleSignUp(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        # Check for errors
        if len(username) > 10:
            messages.error(request, " Username must be under 10 characters")
            return redirect('/signup/')

        if pass1 != pass2:
             messages.error(request, " Passwords do not match")
             return redirect('/signup/')
        
        # Create the user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.save()
        messages.success(request, " Your account has been successfully created")
        return redirect('/login/')

    return render(request, 'signup.html')


def handleLogin(request):
    if request.method == "POST":
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']

        user = authenticate(username=loginusername, password=loginpassword)
        
        if user is not None:
            login(request, user)
            messages.success(request, " Successfully Logged In")
            return redirect('/')
        else:
            messages.error(request, " Invalid credentials, please try again")
            return redirect('/login/')
            
    return render(request, 'login.html')

def handleLogout(request):
    logout(request)
    messages.success(request, " Successfully logged out")
    return redirect('/')

