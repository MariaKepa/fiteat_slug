
# -*- coding: utf-8 -*-
from django.contrib import admin

# Register your models here.

from .models import Category
from .models import Product
# from .models import DiaryEntry


admin.site.register(Category)



admin.site.register(Product)
# admin.site.register(DiaryEntry)