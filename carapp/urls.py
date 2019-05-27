from django.urls import path

from carapp import views
app_name = 'carapp'
urlpatterns = [
    path('car/',views.car,name='car'),
    path('addcar/',views.addcar,name='addcar'),
    path('upcar/',views.upcar,name='upcar'),
    path('car_remove/',views.car_remove,name='car_remove'),
]