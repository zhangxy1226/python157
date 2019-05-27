from django.shortcuts import render,redirect
from userapp.models import BookClassT,BooksT

# Create your views here.
def home(request):

    b1 = BooksT.objects.filter(id__in=range(1,9))
    b2 = BooksT.objects.filter(id__in=range(9,17))
    b3 = BooksT.objects.filter(id__in=range(17,26))
    book_c1 = BookClassT.objects.filter(id__in=range(1, 15))
    book_c2 = BookClassT.objects.filter(id__in=range(16, 65))
    return render(request,'index.html',{'b1':b1,'b2':b2,'b3':b3,'book_c1':book_c1,'book_c2':book_c2})
def book_details(request):
    book_id=request.GET.get('id')
    book=BooksT.objects.filter(id=book_id)[0]
    monery=round(float(book.dd_price)/float(book.price)*10.0,2)
    return render(request,'Book details.html',{'book':book,'monery':monery})

