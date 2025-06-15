from django.db import models

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