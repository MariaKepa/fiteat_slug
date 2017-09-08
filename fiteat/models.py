# # -*- coding: utf-8 -*-
from django.db import models
from django.core.urlresolvers import reverse
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='fotocategory/%Y/%m/%d', blank=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True) 

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('fiteat:product_list_by_category', args=[self.slug])

class Product(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category)
    protein = models.FloatField(default=0.0)
    carbon = models.FloatField(default=0.0)
    fats = models.FloatField(default=0.0)
    calories = models.FloatField(default=0.0)
    weight = models.FloatField(default=100.0)
    slug = models.SlugField(max_length=200, db_index=True, unique=True) 

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('fiteat:product_detail', args=[self.id , self.slug])

# class DiaryEntry(models.Model):
# 	product = models.ForeignKey(Product)
# 	user = models.ForeignKey('auth.User')
# 	weight = models. IntegerField(default=0)
# 	published_date = models.DateTimeField(
#             blank=True, null=True)

# 	def __str__(self):
# 		return str(self.id)
