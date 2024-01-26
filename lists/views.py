from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse

from lists.models import Item, List


# Create your views here.
def home_page(request: HttpRequest):
    return render(request, 'home.html')


def new_list(request: HttpRequest):
    Item.objects.create(text=request.POST['item_text'], list=List.objects.create())
    return redirect('/lists/the-only-list-in-the-world/')


def view_list(request: HttpRequest):
    return render(request, 'list.html', {'items': Item.objects.all()})
