from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

from lists.models import Item


# Create your views here.
def home_page(request: HttpRequest):
    item = Item()
    item.text = request.POST.get('item_text', '')
    item.save()
    
    return render(request, 'home.html', {'new_item_text': request.POST.get('item_text', '')})
