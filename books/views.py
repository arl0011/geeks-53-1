from django.shortcuts import render
from django.http import HttpResponse
def books(request):
    if request.method == 'GET':
        return HttpResponse("Есть что-то магическое в том, как несколько страниц могут перенести тебя в другой мир. Открываешь книгу — и вдруг ты уже не дома на диване, а в Средиземье, Хогвартсе или на борту космического корабля.")

