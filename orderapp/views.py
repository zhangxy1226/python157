from django.shortcuts import render,redirect,HttpResponse

# Create your views here.
from userapp.models import AdrssInfo


def indent(request):
    cart = request.session.get('cart')
    print(cart.allprice,'all')
    who=request.session.get('who')
    if not who:
        who=''
    return render(request,'indent.html',{'cart':cart,'who':who})
def adress(request):
    recipient=request.GET.get('ship_man')
    adress=request.GET.get('ship_adr')
    zip_code=request.GET.get('ship_code')
    tel=request.GET.get('ship_tel')
    phone=request.GET.get('ship_phone')
    adress_info=AdrssInfo(recipient=recipient,adress=adress,zip_code=zip_code,tel=tel,phone=phone).save()
    cart = request.session.get('cart')
    return render(request,'indent ok.html',{'adress':adress_info,'cart':cart})