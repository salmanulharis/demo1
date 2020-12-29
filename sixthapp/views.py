from django.shortcuts import render, HttpResponse, redirect
from .models import Products, Category
from .forms import ProductForm, ProductModelForm, RegistrationForm, EditForm, CategoryForm

from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='/login/')
def home(request):
    products = Products.objects.all()
    categories = Category.objects.all()
    context = {
        'products': products,
        'categories': categories
    }
    return render(request, 'home.html', context)

def show_products(request, id):
    category = Category.objects.get(id=id)
    categories = Category.objects.all()
    products = category.products_set.all()
    context = {
        'products': products,
        'categories': categories
    }
    return render(request, 'show_products.html', context)

@login_required(login_url='/login/')
def add_product(request):
    if request.method == "POST":
        form = ProductModelForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            return redirect('home')
        else:
            return render(request, 'add_product.html', {'form':form})
    else:
        form = ProductModelForm()
        return render(request, 'add_product.html', {'form':form})

@login_required(login_url='/login/')
def edit_product(request, id):
    product = Products.objects.get(id=id)
    if request.method == "POST":
        form = ProductModelForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            return render(request, 'add_product.html', {'form':form})
    else:
        form = ProductModelForm(instance=product)
        return render(request, 'add_product.html', {'form':form})

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            return render(request, 'register.html', {'form':form})
    else:
        form = RegistrationForm()
        return render(request, 'register.html', {'form':form})

@login_required(login_url='/login/')
def edit_user(request):
    if request.method == 'POST':
        form = EditForm(request.POST, instance= request.user)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            return render(request, 'register.html', {'form':form})
    else:
        form = EditForm(instance= request.user)
        return render(request, 'register.html', {'form':form})

@login_required(login_url='/login/')
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user= request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(form.user)
            return redirect('home')
        else:
            return render(request, 'register.html', {'form':form})
    else:
        form = PasswordChangeForm(user= request.user)
        return render(request, 'register.html', {'form':form})

def login_page(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse('username or password incorrect')
    else:
        return render(request, 'login.html')

def logout_fn(request):
    logout(request)
    return redirect('/login/')

@login_required(login_url='/login/')
def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data['name']
            category = Category(name=name)
            category.save()
            return redirect('home')
        else:
            return render(request, 'add_category.html', {'form':form})
    else:
        form = CategoryForm()
        return render(request, 'add_category.html', {'form':form})

def delete_product(request, id):
    product = Products.objects.get(id=id)
    product.delete()
    return redirect('home')

def del_category(request, id):
    category = Category.objects.get(id=id)
    category.delete()
    return redirect('home')