from django.shortcuts import render,redirect
from app01 import models

# Create your views here.

def login(request):
    if request.method == 'POST':
        name = request.POST.get("user")
        password = request.POST.get("password")
        if not name or not password:
            return render(request, 'login.html', {'error':'用户名和密码不能为空'})
        if not models.user.objects.filter(username=name,password=password):
            return render(request,'login.html',{'error':'用户不存在'})
        return redirect('/sc_list/')
    return  render(request, 'login.html')





def sc_list(request):
    sc_list = models.sc_list.objects.all()
    return render(request,'sc_list.html',{'sc_list':sc_list})


def sc_add(request):
    if request.method == "POST":
        scName = request.POST.get("scName")
        if not scName:
            return render(request,'sc_add.html',{'error':'市场名称不能为空'})
        if models.sc_list.objects.filter(sc_name=scName):
            return render(request, 'sc_add.html', {'error': '该市场已存在'})
        scAddress = request.POST.get('scAddress')
        scManager = request.POST.get('scManager')
        scPhone = request.POST.get('scPhone')
        models.sc_list.objects.create(sc_name=scName,sc_address=scAddress,sc_manager=scManager,sc_phone=scPhone)
        return redirect('/sc_list/')
    return render(request,'sc_add.html')


def sc_del(request):
    pk = request.GET.get("id")
    models.sc_list.objects.filter(pk=pk).delete()
    return redirect('/sc_list/')


def sc_edit(request):
    pk = request.GET.get("id")
    sc_obj = models.sc_list.objects.get(pk=pk)
    if request.method == "POST":
        scName = request.POST.get("scName")
        sc_obj.sc_name = scName
        scAddress = request.POST.get('scAddress')
        sc_obj.sc_address = scAddress
        scManager = request.POST.get('scManager')
        sc_obj.sc_manager = scManager
        scPhone = request.POST.get('scPhone')
        sc_obj.sc_phone = scPhone
        sc_obj.save()
        return redirect('/sc_list/')
    return render(request,'sc_edit.html',{'sc_obj':sc_obj})


def store_list(request):
    sc_list = models.sc_list.objects.all()
    return render(request, 'store_list.html', {'store_list': sc_list})


def store_add(request):
    if request.method == "POST":
        sc_Name = request.POST.get("scName")
        fl = request.POST.get("floor")
        store_order = request.POST.get("storeOrder")
        if not sc_Name:
            return render(request,'store_add.html',{'error0':'市场名称不能为空'})
        if not fl:
            return render(request,'store_add.html',{'error1':'楼层不能为空'})
        if not store_order:
            return render(request,'store_add.html',{'error':'档口号不能为空'})
        if models.store_list.objects.filter(store_order=store_order):
            return render(request, 'store_add.html', {'error': '该档口已存在'})
        models.store_list.objects.create(sc_name=sc_Name,floor=fl,store_order=store_order)
        return redirect('/store_list/')
    sc_all = models.sc_list.objects.all()
    return render(request,'store_add.html',{'sc_all':sc_all})


def store_del(request):
    pk = request.GET.get("id")
    models.store_list.objects.filter(pk=pk).delete()
    return redirect('/store_list/')


def store_edit(request):
    pk = request.GET.get("id")
    store_obj = models.store_list.objects.get(pk=pk)
    if request.method == "POST":
        store_obj.scName = request.POST.get("scName")
        store_obj.floor = request.POST.get('floor')
        store_obj.store_order = request.POST.get('store_order')
        store_obj.save()
        return redirect('/store_list/')
    return render(request,'sc_edit.html',{'store_obj':store_obj})