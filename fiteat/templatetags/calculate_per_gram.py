# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import template
register = template.Library()

@register.simple_tag()
def calculate_per_gram(weight, value, *args, **kwargs):
    # you would need to do any localization of the result here
    return weight*value/100