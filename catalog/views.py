from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from catalog.models import Category, Product



def home(request):
    articles = Product.objects.all().order_by('?') # ?= Aleatory
    context = {"articles": articles}
    return render(request, 'home.html', context)

#View to show items.name on navbar and the products on page
def category_detail(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    products = Product.objects.filter(category=category)
    return render(request, "category_detail.html", {
        "category": category,
        "products": products
    })

