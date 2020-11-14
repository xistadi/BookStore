from django.views.generic import TemplateView
from . import models
from products import models as book_models


def create_cart(user, session):
    cart = models.Cart.objects.create(customer=user)
    session['cart_id'] = cart.pk
    return cart


class CartView(TemplateView):
    template_name = 'cart/cart_index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart_id = self.request.session.get('cart_id')
        user = self.request.user
        # get a cart
        if not user.is_authenticated:
            user = None
        if cart_id:
            cart = models.Cart.objects.filter(pk=cart_id).first()
            if not cart:
                cart = create_cart(user, self.request.session)
        else:
            cart = create_cart(user, self.request.session)
        # add a book to the cart
        book_id = self.request.GET.get('book')
        try:
            book_id = int(book_id)
        except:
            pass
        book = book_models.Book.objects.filter(pk=book_id).first()
        if book:
            pass # add to the cart
        else:
            pass # redirect to
        context['cart'] = cart
        context['book'] = book
        return context
