from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse

from lists.models import Item, List


# Create your views here.
def home_page(request: HttpRequest):
    return render(request, 'home.html')


def new_list(request: HttpRequest):
    list_ = List.objects.create()
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect(f'/lists/{list_.id}/')


def view_list(request: HttpRequest, list_id):
    list_ = List.objects.get(id=list_id)
    return render(request, 'list.html', {'list': list_})


def add_item(request: HttpRequest, list_id):
    list_ = List.objects.get(id=list_id)
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect(f'/lists/{list_id}/')
