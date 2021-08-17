from .models import Book

def return_book(request):
    return {
        'books':Book.objects.all(),
    }