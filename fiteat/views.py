# # -*- coding: utf-8 -*-
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth import authenticate, login
from django.views.generic import View
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm
from .models import Category
from .models import Product
# from .models import DiaryEntry
from .filters import ProductFilter



# # Create your views here.

def first_page(request):
    return render (request, 'fiteat/first_page.html', {})

    
# def product(request):
#     categorys = Category.objects.all()
#     return render (request, 'fiteat/products.html', {'categorys':categorys})

def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products =Product.objects.all()
    if category_slug:
        category = get_object_or_404(Category, slug=catgeory_slug)
        products = products.filter(category=category)
    return render (request, 'fiteat/products.html', {'categories':categories, 'category':category, 'products':products})


def product_detail(request, id):
    product_list = Product.objects.filter(category__id=id)
    return render(request,'fiteat/product_detail.html', {'products':product_list})

def contact(request):
    return render(request, 'fiteat/nav_menu/contact.html', {})

def aboutme(request):
    return render(request, 'fiteat/nav_menu/aboutme.html', {})

def statute(request):
    return render(request, 'fiteat/nav_menu/statute.html', {})

def tips(request):
    return render(request, 'fiteat/nav_menu/tips.html', {})

def diary(request):

    diary_entries = DiaryEntry.objects.filter(user = request.user)
    return render(request, 'fiteat/nav_menu/diary.html', {'diary_entries': diary_entries})

def body_weight(request):
    return render(request, 'fiteat/nav_menu/body_weight.html', {})

def edit_panel(request):
    return render(request, 'fiteat/nav_menu/edit_panel.html', {})

def profile(request):
    return render(request, 'fiteat/profile.html', {})

def calories(request):
    return render(request, 'fiteat/calories_person.html', {})

# ----------REGISTRATION------

def register(request):
    if request.method == "POST":
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save()
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request, 'fiteat/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'fiteat/register.html', {'user_form':user_form})


# ---------------LOGIN---------
@login_required
def dashboard(request):
    return render(request, 'fiteat/dashboard.html', {})

def remove_diary_entry(request, id):
    DiaryEntry.objects.get(id=id).delete()
    return diary(request)
# # ---------------WYSZUKIWANIE PRODUKTU-----------------
   


def search(request):
     product_list = Product.objects.all()
     product_filter = ProductFilter(request.GET, queryset=product_list)
     return render(request, 'fiteat/search.html', {'filter': product_filter})

