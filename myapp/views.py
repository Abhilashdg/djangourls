from django.shortcuts import render
from django.http import HttpResponse
from .models import  book

# Create your views here.
def index(request):
    my_book = book.objects.all()
    context = {
        'my_book': my_book
    }
    return render(request, 'myapp/index.html', context)

def detail(request, book_id):
    books = book.objects.get(id=book_id)
    return render(request, 'myapp/detail.html', {'books':books})

def products(request):
    return HttpResponse('Products')