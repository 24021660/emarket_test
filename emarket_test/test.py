from . import forms
from sqlmodels.models import User
from django.shortcuts import render_to_response,render


def test(request):
    ctx={}
    if request.POST:
        if request.POST['hide']=='1':
            username=User(username=request.POST['username'],password=request.POST['password'])
            username.save()
            ctx['rlt']=request.POST['username']
        elif request.POST['hide']=='2':
            username=User.objects.get(username=request.POST['login_username'],password=request.POST['login_password'])
            for var in username:
                ctx['m']=var.username
            if str(username)!='<QuerySet []>':
                ctx['rlt']='登陆成功'
            else:
                ctx['rlt'] = '登陆失败'
    return render(request,'index.html',ctx)