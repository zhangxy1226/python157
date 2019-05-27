from django.urls import path

from homeapp import views

app_name='homeapp'
urlpatterns = [
    path('home/',views.home,name='home'),
    path('book_details/',views.book_details,name='book_details')
]