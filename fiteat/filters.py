from django import forms
from .models import Product, Category
import django_filters

class ProductFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')  
    # category__name = django_filters.ModelChoiceField(queryset=Category.objects.all(), initial=0)
    # categorys = django_filters.(queryset= Category.objects.all(), widget=forms.CheckboxSelectMultiple)
    
    class Meta:
        model = Product
        fields = ['name', 'category']