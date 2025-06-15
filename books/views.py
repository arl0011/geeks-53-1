from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from . import models

def books_list_view(request):
    if request.method =='GET':
        books_list = models.Books.objects.all().order_by('-id')
        context = {
            'books_list':books_list,
        }
        return render(request,template_name='books.html',context=context)

def books_detail_view(request,id):
    if request.method == 'GET':
        book_id = get_object_or_404(models.Books,id=id)
        context={
            'book_id':book_id,
        }
        return render(request,template_name='book_detail.html',context=context)
        






def books(request):
    if request.method == 'GET':
        return HttpResponse("Есть что-то магическое в том, как несколько страниц могут перенести тебя в другой мир. Открываешь книгу — и вдруг ты уже не дома на диване, а в Средиземье, Хогвартсе или на борту космического корабля.")
