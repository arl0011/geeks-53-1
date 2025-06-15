from django.urls import path
from . import views

urlpatterns = [
    path('news_books/',views.books_list_view,name='news_books'),
    path('news_books/<int:id>/',views.books_detail_view,name='news_books_detail'),
    path('books/',views.books, name='books'),
]