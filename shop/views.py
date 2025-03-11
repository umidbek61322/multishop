from django.shortcuts import render
from django.views.generic import ListView

from shop.models import *

class Index(ListView):
    model = SubCategory
    context_object_name = "subcategories"
    template_name = "shop/index.html"
    extra_context = {
        "title":"Delete"
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categories = Category.objects.all()
        subcategories = SubCategory.objects.all()
        offers = Offer.objects.all()
        products = Product.objects.all()
        data = {}
        data["categories"] = categories
        data["subcategories"] = subcategories
        data["offers"] = offers
        data["products"] = products
        context["data"] = data
        return context



