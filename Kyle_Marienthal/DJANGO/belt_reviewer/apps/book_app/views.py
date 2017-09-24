from django.shortcuts import render
from ..log_reg_app.models import User

# Create your views here.
def book(request):
    print User.objects.all()
    print '*****youre in the success method of book_app*****'
    return render(request, 'book_app/books.html')
