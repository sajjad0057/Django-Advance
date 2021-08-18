from django.shortcuts import render
from .models import Book,Author,BookInstance,Genre
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from catalog import models


# Create your views here.
def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    # The 'all()' is implied by default.
    num_authors = Author.objects.count()

    # session 

    num_visits = request.session.get('num_visits',0)
    #print('num_visits------> ',num_visits)
    request.session['num_visits'] = num_visits + 1

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_visits':num_visits,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)





# class BookListView(generic.ListView):
#     model = Book
#     context_object_name = 'book_list'   # your own name for the list as a template variable
#     queryset = Book.objects.filter(title__icontains='a')[:5] # Get 5 books containing the title war
#     template_name = 'books/book_list.html'  # Specify your own template name/location


# class BookListView(generic.ListView):
#     model = Book

#     def get_queryset(self):
#         return Book.objects.filter(title__icontains='war')[:5] # Get 5 books containing the title war



class BookListView(LoginRequiredMixin,generic.ListView):
    model = Book
    paginate_by = 2
    def get_queryset(self):
        return Book.objects.filter(title__icontains='a')[:5] # Get 5 books containing the title war

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super().get_context_data(**kwargs)
        # Create any data and add it to the context
        context['some_data'] = 'This is just some data'
        return context



class BookDetailView(LoginRequiredMixin,generic.DetailView):
    model = Book



class AuthorListView(LoginRequiredMixin,generic.ListView):
    model = Author
    context_object_name = 'author_list'
    template_name = 'author_list.html'


class AuthorDetailView(generic.DetailView):
    model = Author




class LoanedBooksByUserListView(LoginRequiredMixin,generic.ListView):
    """Generic class-based view listing books on loan to current user."""
    model = BookInstance
    template_name ='catalog/bookinstance_list_borrowed_user.html'
    paginate_by = 10

    def get_queryset(self):
        return BookInstance.objects.filter(borrower=self.request.user).filter(status__exact='o').order_by('due_back')
    









