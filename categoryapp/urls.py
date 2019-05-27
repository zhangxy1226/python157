from django.urls import path

from categoryapp import views
app_name='categoryapp'
urlpatterns = [
    path('booklist/',views.booklist,name='booklist'),
    path('book_list/',views.book_list,name='book_list'),
]