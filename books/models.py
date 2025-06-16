from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Books(models.Model):
    title = models.CharField(max_length=100,verbose_name='напишите название книги')
    image = models.ImageField(upload_to='books/',verbose_name='загрузите картинку')
    description =models.TextField(verbose_name='напишите описание книги')
    BOOK_GENRE = (
        ('Drama','Drama'),
        ('fantasy','fantasy'),
        ('thriller','thriller'),
    )
    book_genre = models.CharField(max_length=100,choices=BOOK_GENRE)


    created_ad = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title  
    
    class Meta:
        verbose_name = 'книгу'
        verbose_name_plural = 'книг'



class Reviews(models.Model):
    choise_books = models.ForeignKey(Books,on_delete=models.CASCADE,related_name='book',verbose_name='выберите книгу',null=True)
    text = models.TextField(verbose_name='напишите отзыв')
    created_ad = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey( User,on_delete=models.CASCADE,null=True,blank=True,verbose_name='Автор')

    mark = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)],null=True,blank=True,verbose_name='Оценка (от 1 до 5)')

    def __str__(self):
        return f'{self.choise_books}-{self.text}'