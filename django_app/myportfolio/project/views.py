from django.shortcuts import render, redirect
from .models import Product
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .forms import CustomUserCreationForm
#from .models import CartItem


# Create your views here.
def home_screen(request):
    print(request.headers)
    return render (request, 'index.html', {})


def about_screen(request):
    print(request.headers)
    return render (request, 'about.html', {})


def blog_screen(request):
    print(request.headers)
    return render (request, 'blog.html', {})


def cart_screen(request):
    print(request.headers)
    return render (request, 'cart.html', {})


def checkout_screen(request):
    print(request.headers)
    return render (request, 'checkout.html', {})


def contact_screen(request):
    print(request.headers)
    return render (request, 'contact.html', {})


def services_screen(request):
    print(request.headers)
    return render (request, 'services.html', {})


def shop_screen(request):
    print(request.headers)
    return render (request, 'shop.html', {})


def thankyou_screen(request):
    print(request.headers)
    return render (request, 'thankyou.html', {})


def login_screen(request):
    print(request.headers)
    return render (request, 'login.html', {})

def logout_screen(request):
    print(request.headers)
    return render (request, 'logout.html', {})

def register_screen(request):
    print(request.headers)
    return render (request, 'register.html', {})

def password_reset_screen(request):
    print(request.headers)
    return render (request, 'password_reset.html', {})

def product_list_screen(request):
    products = [
        {
            'name': f'Product {i}',
            'price': i * 10,
            'description': f'Description for Product {i}',
        } for i in range(1, 500)
    ]
    return render(request, 'product_list.html', {'products': products})


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')  # Redirect to the home page or any other page
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})



def add_to_cart(request):
    if request.method == 'POST':
        name = request.POST['name']
        price = request.POST['price']
        # Add the product to the cart, either by creating a CartItem instance or updating session/cart data
        # Redirect to the cart page or product list page
    return redirect('product_list')
