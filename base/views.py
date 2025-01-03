from django.shortcuts import render
from base.models import *
def home(request):
    category = Category.objects.all()
    banners = Banner.objects.all()
    items = Item.objects.all()


    context = {
        'cats' : category,
        'banners': banners,
        'items' : items
    }
    return render(request, 'home.html', context)


def product_view(request, slug):
    get_item = Item.objects.get(slug=slug)
    get_pack = ItemPackage.objects.filter(item=get_item)

    context = {
        'item' : get_item,
        'package' : get_pack
    }
    return render(request, 'product_view.html', context)

def signup(request):
    return render(request, 'signup.html')