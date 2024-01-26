from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

from lists.models import Item


# Create your views here.
def home_page(request: HttpRequest):
    if request.method == 'POST':
        new_item_text = request.POST['item_text']
        Item.objects.create(text=new_item_text)
    else:
        new_item_text = ''
    
    return render(request, 'home.html', {'new_item_text': request.POST.get('item_text', '')})
