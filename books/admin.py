from django.contrib import admin
from .models import Books
# Register your models here.


class BooksAdmin(admin.ModelAdmin):
    list_filter = ['narxi', 'author']
    list_display = ['title', 'author']
    search_fields = ['title']

admin.site.register(Books, BooksAdmin)