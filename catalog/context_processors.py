from .models import Book


#using context_proccessor we can access our context globally any template

def return_book(request):
    return {
        'books':Book.objects.all(),
    }