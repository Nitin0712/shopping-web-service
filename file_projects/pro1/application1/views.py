from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ProductForm
from .models import product, product_cart, product_quantity
from random import randint
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.sessions.models import Session


# Create your views here.
def index(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            # handle_upload_file(request.FILES)
            form.save()
            return redirect(view_product)
    else:
        product = ProductForm()
        return render(request, 'form.html', {'form': product})


def view_product(request):
    if 'is_logged' in request.session:
        data = product.objects.all()
        return render(request, 'home.html', {'pro_data': data, 'user_login': True})
    else:
        data = product.objects.all()
        return render(request, 'home.html', {'pro_data': data})


def edit_product(request, id):
    editData = product.objects.get(pk=id)
    return render(request, 'edit.html', {'editForm': editData})


def update_product(request, id):
    editData = product.objects.get(id=id)
    form = ProductForm(request.POST, request.FILES, instance=editData)
    if form.is_valid():
        form.save()
        return redirect(view_product)
    return render(request, "emp_list.html", {'editForm': editData})


def add_to_cart(request):
    if request.method == 'POST':
        cart_product_id = request.POST['cart_product_id']
        cart_usr_id = request.POST['cart_usr_id']
        try:
            check_cart_item = product_cart.objects.get(cart_product_id=cart_product_id, cart_usr_id=cart_usr_id)
            if check_cart_item.cart_quantity > 0:
                cart_quantity = check_cart_item.cart_quantity + 1
                update_cart = product_cart.objects.filter(cart_product_id=cart_product_id, cart_usr_id=cart_usr_id).\
                    update(cart_quantity=cart_quantity)
        except product_cart.DoesNotExist:
            cart_quantity = 1
            update_cart = product_cart.objects.create(cart_product_id=cart_product_id, cart_usr_id=cart_usr_id,
                                                      cart_quantity=cart_quantity)
        return redirect('home')
    else:
        return redirect('home')


def view_cart(request, id):
    cart_data = product_cart.objects.filter(cart_usr=id)
    return render(request, 'addtocart.html', {'carts_data': cart_data})


def regview(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email1']
        password = request.POST['password']
        c_password = request.POST['c_password']
        user_form = User(request.POST or None)
        if password != c_password:
            messages.info(request, 'Password Does not match')
            return redirect('register')
        elif User.objects.filter(username=username).exists():
            messages.info(request, 'Username already taken')
            return redirect('register')
        elif User.objects.filter(email=email).exists():
            messages.info(request, 'Email ID already taken')
            return redirect('register')
        else:
            form = User.objects.create_user(first_name=first_name, last_name=last_name, email=email,
                                            username=username, password=password)
            form.save()
            messages.info(request, 'Registration successfully')
            return redirect(view_product)
    else:
        return render(request, 'login.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            request.session['is_logged'] = True  # set session key
            # request.session.set_expiry(10) # set session expire time
            auth.login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login')
    else:
        return render(request, 'login.html', {'login': login})


def logout_user(request):
    logout(request)
    return redirect('home')


def get_search_data(request):
    search = request.GET['search']
    data = product.objects.filter(product_name__contains=search)
    if data:
        return render(request, 'home.html', {'pro_data': data})
    else:
        return render(request, 'home.html', {'no_search_data': 'No Data Found'})
















# def generate_otp(request):
#     return HttpResponse(request)
#     otp = randint(1000, 9999)
#     message = "Here is your OTP {} for registration \n Don't share it with anyone".format(otp)
#     number = request.GET['number']
#     api = request.get(
#         'http://api.textlocal.in/send/?username=YOUR USERNAME&hash=YOUR HASH KEY&message=' + message + '&sender=TXTLCL&numbers=91"' + number + '"&test=0')
#     return HttpResponse(otp)


"""Django Cookies Example"""
# def setcookie(request):
#     response = HttpResponse('set cookie')
#     response.set_cookie('java-tutorial', 'javatpoint.com')
#     return response
#
#
# def getcookie(request):
#     tutorial = request.COOKIES['java-tutorial']
#     return HttpResponse(tutorial)

"""Django CSV Example"""
# def importcsv(request):
#     response = HttpResponse(content_type='text/csv')
#     response['Content-Disposition'] = 'attachment; file = "one.csv"'
#     writer = csv.writer(response)
#     writer.writerow(['1001', 'John', 'Domil', 'CA'])
#     writer.writerow(['1002', 'Amit', 'Mukharji', 'LA', '"Testing"'])
#     return response
