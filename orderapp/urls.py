from django.urls import path

from orderapp import views
app_name='orderapp'
urlpatterns = [
    path('indent/', views.indent,name='indent'),
    path('adress/', views.adress,name='adress'),
]