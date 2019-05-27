from django.core.paginator import Paginator
from django.shortcuts import render,redirect
# Create your views here.
from userapp.models import BooksT, BookClassT, User


def booklist(request):
    o_id=request.GET.get('o_id')
    t_id=request.GET.get('t_id')
    book_c1 = BookClassT.objects.filter(id__in=range(1, 15))
    book_c2 = BookClassT.objects.filter(id__in=range(16, 65))
    num = request.GET.get('page')
    if not num:
        num = 1
    if o_id and t_id == 'None' or o_id and t_id is None:
        gps1=BookClassT.objects.get(id=o_id)
        b = BooksT.objects.filter(pid__pid__in=o_id)
        pagtor = Paginator(b,per_page=3)
        page = pagtor.page(num)
        return render(request,'booklist.html',{'page':page,'stu':1,'gps1':gps1,'book_c1':book_c1,'book_c2':book_c2,'o_id':o_id,'t_id':t_id,'pagtor':pagtor})
    elif t_id and o_id == 'None' or t_id and o_id is None:
        books1 = BooksT.objects.filter(pid=t_id)
        gps2=BookClassT.objects.get(id=t_id)
        ogps1=BookClassT.objects.get(id=BookClassT.objects.get(id=t_id).pid)
        bb = BooksT.objects.filter(pid=t_id)
        pagtor = Paginator(bb,per_page=3)
        page = pagtor.page(num)
        return render(request, 'booklist.html', {'page':page,'books1':books1,'stu':2,'ogps1':ogps1,'gps2':gps2,'book_c1':book_c1,'book_c2':book_c2,'o_id':o_id,'t_id':t_id,'pagtor':pagtor})
def book_list(request):
    #获取 页面书籍id
    on_id=request.GET.get('id')
    #获取数据库每本书的ID
    book_id=BooksT.objects.get(pid=on_id)
    #通过每本书的id查找二级分类
    t_id=BookClassT.objects.get(pid=book_id)
     #通过二级分类的id查找以及分类照片那个书的id
    o_id=BookClassT.objects.get(id=t_id)







