from django.urls import path

from userapp import views
app_name='userapp'
urlpatterns = [
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('logic/',views.logic,name='logic'),
    path('checkname/', views.checkname, name='checkname'),
    path('pwd/', views.pwd, name='pwd'),
    path('pwd2/', views.pwd2, name='pwd2'),
    path('getcaptcha/', views.getcaptcha, name='getcaptcha'),
    path('click_reg/', views.click_reg, name='click_reg'),
    path('reglogic/', views.reglogic, name='reglogic'),
]