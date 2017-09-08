from decimal import Decimal
from django.conf import settings
from fiteat.models import Product

class Cart(object):

    def __init__(self, request):
        """
        Inicjalizacja koszyka na zakupy.
        """
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # Zapis pustego koszyka na zakupy w sesji.
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, product, quantity=1, update_quantity=False):
        """
        Dodanie produktu do koszyka lub zmiana jego ilości.
        """
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0,
                                      'weight': str(product.weight),
                                      'protein': str(product.protein)}
        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()

    def save(self):
        # Uaktualnienie koszyka sesji.
        self.session[settings.CART_SESSION_ID] = self.cart
        # Oznaczenie sesji jako "zmodyfikowanej", aby upewnić się o jej zapisaniu.
        self.session.modified = True

    def remove(self, product):
        """
        Usunięcie produktu z koszyka na zakupy.
        """
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def __iter__(self):
        """
        Iteracja przez elementy koszyka na zakupy i pobranie produktów
        z bazy danych.
        """
        product_ids = self.cart.keys()
        # Pobranie obiektów produktów i dodanie ich do koszyka na zakupy.
        products = Product.objects.filter(id__in=product_ids)
        for product in products:
            self.cart[str(product.id)]['product'] = product

        for item in self.cart.values():
            item['weight'] = Decimal(item['weight'])
            item['total_weight'] = (item['weight']/100) * Decimal(item['quantity'])
            # item['total_protein'] = (item['protein'])
            yield item

    def get_total_weight(self):
         return sum(Decimal(item['quantity']) for item in self.cart.values())
    
    # def get_total_weight1(self):
    #      return sum(Decimal(item['total_protein']) for item in self.cart.values())

    def clear(self):
        # Usunięcie koszyka na zakupy z sesji.
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True