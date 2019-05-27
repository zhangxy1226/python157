import string
import random

from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse

from userapp.captcha.image import ImageCaptcha
from userapp.models import User


def register(request):
    return render(request, 'register.html')


def login(request):
    return render(request, 'login.html')
def logic(request):
    name=request.POST.get('txtUsername')
    pwd=request.POST.get('txtPassword')
    user=User.objects.get(name=name,pwd=pwd)

    return redirect('/homeapp/home')

def reglogic(request):
    username = request.POST.get('txt_username')
    txt_pwd = request.POST.get('txt_password')
    m_user = User.objects.filter(name=username)
    request.session['who'] = username
    if m_user:
        return redirect('userapp:register')
    else:
        user_info = User(name=username, pwd=txt_pwd).save()
        url = reverse("userapp:click_reg") + "?uname="+username
        return redirect(url)

def checkname(request):
    inputname = request.POST.get('inputname')
    user = User.objects.filter(name=inputname)
    if user:
        return HttpResponse('no')
    else:
        if not inputname:
            return HttpResponse('empty')
        else:
            return HttpResponse('ok')

def pwd(request):
    user_pwd1 = request.POST.get('inputpwd')
    if not user_pwd1:
        return HttpResponse('empty')
    else:
        return HttpResponse('q')

def pwd2(request):
    user_pwd1 = request.POST.get('inputpwd')
    userpwd2 = request.POST.get('inputpwd2')
    if user_pwd1 == userpwd2:
        return HttpResponse('ok')
    else:
        return HttpResponse('no')

def getcaptcha(request):
    image = ImageCaptcha()
    code = random.sample(string.ascii_letters+string.digits,4)
    random_code = ''.join(code)
    request.session['code'] = random_code
    data = image.generate(random_code)
    print(random_code)
    return HttpResponse(data,'image/png')
def click_reg(request):
    uname = request.GET.get('uname')
    return render(request,'register ok.html',{'uname':uname})
