from django.shortcuts import render
from . models import Device, Fan
from django.core.paginator import Paginator
from django.db.models import Q


# Create your views here.





def index(request):
#fanstatus와 fanhealth 합치기
    data_device = Device.objects.all()
    #추후 svr_list에 따라 device = num 부분만 변경하여 사용하면 됨! 
    sdp = Fan.objects.filter(device__in=range(1,5)).distinct().exclude(Q(fan_health__icontains='ok') | Q(fan_status__icontains='absent')).values('fan_name', 'fan_status', 'fan_health')
    fdp = Fan.objects.filter(device__in=range(5,9)).distinct().exclude(Q(fan_health__icontains='ok') | Q(fan_status__icontains='absent')).values('fan_name', 'fan_status', 'fan_health')
    drf = Fan.objects.filter(device__in=range(9,13)).distinct().exclude(Q(fan_health__icontains='ok') | Q(fan_status__icontains='absent')).values('fan_name', 'fan_status', 'fan_health')
    sdr = Fan.objects.filter(device__in=range(13,17)).distinct().exclude(Q(fan_health__icontains='ok') | Q(fan_status__icontains='absent')).values('fan_name', 'fan_status', 'fan_health')
    efs = Fan.objects.filter(device__in=range(17,21)).distinct().exclude(Q(fan_health__icontains='ok') | Q(fan_status__icontains='absent')).values('fan_name', 'fan_status', 'fan_health')
    rcom = Fan.objects.filter(device__in=range(21,25)).distinct().exclude(Q(fan_health__icontains='ok') | Q(fan_status__icontains='absent')).values('fan_name', 'fan_status', 'fan_health')
    app = Fan.objects.filter(device__in=(25,26)).distinct().exclude(Q(fan_health__icontains='ok') | Q(fan_status__icontains='absent')).values('fan_name', 'fan_status', 'fan_health')
    nms = Fan.objects.filter(device__in=(27,28)).distinct().exclude(Q(fan_health__icontains='ok') | Q(fan_status__icontains='absent')).values('fan_name', 'fan_status', 'fan_health')
    was = Fan.objects.filter(device__in=(29,30)).distinct().exclude(Q(fan_health__icontains='ok') | Q(fan_status__icontains='absent')).values('fan_name', 'fan_status', 'fan_health')
    etc = Fan.objects.filter(device__in=range(31,34)).distinct().exclude(Q(fan_health__icontains='ok') | Q(fan_status__icontains='absent')).values('fan_name', 'fan_status', 'fan_health')
    test = Fan.objects.filter(device__in=range(34,41)).distinct().exclude(Q(fan_health__icontains='ok') | Q(fan_status__icontains='absent')).values('fan_name', 'fan_status', 'fan_health')

    context = {'data_device' : data_device, 'sdp' : sdp, 'fdp' : fdp, 'drf' : drf, 'sdr' : sdr, 'efs' : efs, 'rcom' : rcom, 'app' : app, 'nms' : nms, 'was' : was, 'etc': etc, 'test' : test,}
    return render(request, 'sys_mon/index.html', context)

def sdp(request):
    data_device = Device.objects.all()
    sdp = Fan.objects.filter(device__in=range(1,5)).distinct().exclude(Q(fan_health__icontains='ok') | Q(fan_status__icontains='absent')).values('fan_name', 'fan_status', 'fan_health')
    o1sdp01 = Fan.objects.filter(device=1).distinct().values('fan_name', 'fan_status', 'fan_health') # device_id = 2 인 값 중에서 중복 제거 후 출력
    o1sdp02 = Fan.objects.filter(device=2).distinct().values('fan_name', 'fan_status', 'fan_health')
    o1sdp03 = Fan.objects.filter(device=3).distinct().values('fan_name', 'fan_status', 'fan_health')
    o1sdp04 = Fan.objects.filter(device=4).distinct().values('fan_name', 'fan_status', 'fan_health')
    context = {'o1sdp01' : o1sdp01, 'o1sdp02' : o1sdp02, 'o1sdp03' : o1sdp03, 'o1sdp04' : o1sdp04, 'data_device' : data_device, 'sdp' : sdp,}
    return render(request, 'sys_mon/sdp.html', context)
def fdp(request):
    data_device = Device.objects.all()
    fdp = Fan.objects.filter(device__in=range(5,9)).distinct().exclude(Q(fan_health__icontains='ok') | Q(fan_status__icontains='absent')).values('fan_name', 'fan_status', 'fan_health')    
    o1fdp01 = Fan.objects.filter(device=5).distinct().values('fan_name', 'fan_status', 'fan_health')
    o1fdp02 = Fan.objects.filter(device=6).distinct().values('fan_name', 'fan_status', 'fan_health')
    o1fdp03 = Fan.objects.filter(device=7).distinct().values('fan_name', 'fan_status', 'fan_health')
    o1fdp04 = Fan.objects.filter(device=8).distinct().values('fan_name', 'fan_status', 'fan_health') # device_id = 1 인 값 중에서 중복 제거 후 출력
    context = {'o1fdp01' : o1fdp01, 'o1fdp02' : o1fdp02, 'o1fdp03' : o1fdp03, 'o1fdp04' : o1fdp04, 'data_device' : data_device, 'fdp' : fdp,}
    return render(request, 'sys_mon/fdp.html', context)

def drf(request):
    data_device = Device.objects.all()
    drf = Fan.objects.filter(device__in=range(9,13)).distinct().exclude(Q(fan_health__icontains='ok') | Q(fan_status__icontains='absent')).values('fan_name', 'fan_status', 'fan_health')
    o1drf01 = Fan.objects.filter(device=9).distinct().values('fan_name', 'fan_status', 'fan_health')
    o1drf02 = Fan.objects.filter(device=10).distinct().values('fan_name', 'fan_status', 'fan_health')
    o1drf03 = Fan.objects.filter(device=11).distinct().values('fan_name', 'fan_status', 'fan_health')
    t1drf05 = Fan.objects.filter(device=12).distinct().values('fan_name', 'fan_status', 'fan_health') # device_id = 1 인 값 중에서 중복 제거 후 출력
    context = {'o1drf01' : o1drf01, 'o1drf02' : o1drf02, 'o1drf03' : o1drf03, 't1drf05' : t1drf05, 'data_device' : data_device, 'drf' : drf,}
    return render(request, 'sys_mon/drf.html', context)

def sdr(request):
    data_device = Device.objects.all()
    sdr = Fan.objects.filter(device__in=range(13,17)).distinct().exclude(Q(fan_health__icontains='ok') | Q(fan_status__icontains='absent')).values('fan_name', 'fan_status', 'fan_health')
    o1sdr01 = Fan.objects.filter(device=13).distinct().values('fan_name', 'fan_status', 'fan_health')
    o1sdr02 = Fan.objects.filter(device=14).distinct().values('fan_name', 'fan_status', 'fan_health')
    o1sdr03 = Fan.objects.filter(device=15).distinct().values('fan_name', 'fan_status', 'fan_health')
    o1sdr04 = Fan.objects.filter(device=16).distinct().values('fan_name', 'fan_status', 'fan_health') # device_id = 1 인 값 중에서 중복 제거 후 출력
    context = {'o1sdr01' : o1sdr01, 'o1sdr02' : o1sdr02, 'o1sdr03' : o1sdr03, 'o1sdr04' : o1sdr04, 'data_device' : data_device, 'sdr' : sdr,}
    return render(request, 'sys_mon/sdr.html', context)


def efs(request):
    data_device = Device.objects.all()
    efs = Fan.objects.filter(device__in=range(17,21)).distinct().exclude(Q(fan_health__icontains='ok') | Q(fan_status__icontains='absent')).values('fan_name', 'fan_status', 'fan_health')
    o1efs01 = Fan.objects.filter(device=17).distinct().values('fan_name', 'fan_status', 'fan_health')
    o1efs02 = Fan.objects.filter(device=18).distinct().values('fan_name', 'fan_status', 'fan_health')
    o1efs03 = Fan.objects.filter(device=19).distinct().values('fan_name', 'fan_status', 'fan_health')
    o1efs04 = Fan.objects.filter(device=20).distinct().values('fan_name', 'fan_status', 'fan_health') # device_id = 1 인 값 중에서 중복 제거 후 출력
    context = {'o1efs01' : o1efs01, 'o1efs02' : o1efs02, 'o1efs03' : o1efs03, 'o1efs04' : o1efs04, 'data_device' : data_device, 'efs' : efs,}
    return render(request, 'sys_mon/efs.html', context)


def rcom(request):
    data_device = Device.objects.all()
    rcom = Fan.objects.filter(device__in=range(21,25)).distinct().exclude(Q(fan_health__icontains='ok') | Q(fan_status__icontains='absent')).values('fan_name', 'fan_status', 'fan_health')
    o1cs0a = Fan.objects.filter(device=21).distinct().values('fan_name', 'fan_status', 'fan_health')
    o1cs0b = Fan.objects.filter(device=22).distinct().values('fan_name', 'fan_status', 'fan_health')
    o1cs1a = Fan.objects.filter(device=23).distinct().values('fan_name', 'fan_status', 'fan_health')
    o1cs1b = Fan.objects.filter(device=24).distinct().values('fan_name', 'fan_status', 'fan_health') # device_id = 1 인 값 중에서 중복 제거 후 출력
    context = {'o1cs0a' : o1cs0a, 'o1cs0b' : o1cs0b, 'o1cs1a' : o1cs1a, 'o1cs1b' : o1cs1b, 'data_device' : data_device, 'rcom' : rcom,}
    return render(request, 'sys_mon/rcom.html', context)
def app(request):
    data_device = Device.objects.all()
    app = Fan.objects.filter(device__in=(25,26)).distinct().exclude(Q(fan_health__icontains='ok') | Q(fan_status__icontains='absent')).values('fan_name', 'fan_status', 'fan_health')
    o1app01 = Fan.objects.filter(device=25).distinct().values('fan_name', 'fan_status', 'fan_health')
    o1app02 = Fan.objects.filter(device=26).distinct().values('fan_name', 'fan_status', 'fan_health')
    context = {'o1app01' : o1app01, 'o1app02' : o1app02, 'data_device' : data_device, 'app' : app,}
    return render(request, 'sys_mon/app.html', context)
def nms(request):
    data_device = Device.objects.all()
    nms = Fan.objects.filter(device__in=(27,28)).distinct().exclude(Q(fan_health__icontains='ok') | Q(fan_status__icontains='absent')).values('fan_name', 'fan_status', 'fan_health')
    m1nms01 = Fan.objects.filter(device=27).distinct().values('fan_name', 'fan_status', 'fan_health')
    m1nms02 = Fan.objects.filter(device=28).distinct().values('fan_name', 'fan_status', 'fan_health')
    context = {'m1nms01' : m1nms01, 'm1nms02' : m1nms02, 'data_device' : data_device,'nms' : nms}
    return render(request, 'sys_mon/nms.html', context)
def was(request):
    data_device = Device.objects.all()
    was = Fan.objects.filter(device__in=(29,30)).distinct().exclude(Q(fan_health__icontains='ok') | Q(fan_status__icontains='absent')).values('fan_name', 'fan_status', 'fan_health')
    o1was01 = Fan.objects.filter(device=29).distinct().values('fan_name', 'fan_status', 'fan_health')
    o1was02 = Fan.objects.filter(device=30).distinct().values('fan_name', 'fan_status', 'fan_health')
    context = {'o1was01' : o1was01, 'o1was02' : o1was02, 'data_device' : data_device,'was' : was}
    return render(request, 'sys_mon/was.html', context)
def etc(request): #byp, tsv, pms
    data_device = Device.objects.all()
    etc = Fan.objects.filter(device__in=range(31,34)).distinct().exclude(Q(fan_health__icontains='ok') | Q(fan_status__icontains='absent')).values('fan_name', 'fan_status', 'fan_health')
    o1byp01 = Fan.objects.filter(device=31).distinct().values('fan_name', 'fan_status', 'fan_health')
    t1tsv01 = Fan.objects.filter(device=32).distinct().values('fan_name', 'fan_status', 'fan_health')
    m1pms01 = Fan.objects.filter(device=33).distinct().values('fan_name', 'fan_status', 'fan_health')
    context = {'o1byp01' : o1byp01, 't1tsv01' : t1tsv01, 'm1pms01' : m1pms01, 'data_device' : data_device, 'etc' : etc,}
    return render(request, 'sys_mon/etc.html', context)

def log(request):
    page = request.GET.get('page', '1')
    kw = request.GET.get('kw', '')
    sd = request.GET.get('sd', '')
    ed = request.GET.get('ed', '')
    dv = request.GET.get('dv', '')
    data_fan = Fan.objects.order_by('-created_time')
    if kw or dv:
        if sd:
            data_fan = data_fan.filter(
                Q(device__svr_name__icontains=dv),
                Q(fan_status__icontains=kw)|
                Q(fan_health__icontains=kw),
                Q(created_time__gte=sd),
                Q(created_time__lte=ed),
            ).distinct()
        else:
            data_fan = data_fan.filter(
                Q(device__svr_name__icontains=dv),
                Q(fan_status__icontains=kw)|
                Q(fan_health__icontains=kw),
            ).distinct()            
    paginator = Paginator(data_fan, 30)
    page_obj = paginator.get_page(page)
    data_device = Device.objects.all()

    context = {'data_device' : data_device, 'data_fan' : page_obj, 'kw' : kw, 'page':page, 'sd':sd, 'ed':ed, 'dv':dv }
    return render(request, 'sys_mon/log.html', context)

def test(request):
    data_device = Device.objects.all()
    test = Fan.objects.filter(device__in=range(34,41)).distinct().exclude(Q(fan_health__icontains='ok') | Q(fan_status__icontains='absent')).values('fan_name', 'fan_status', 'fan_health')
    e1sim01 = Fan.objects.filter(device=34).distinct().values('fan_name', 'fan_status', 'fan_health')
    e1sdr05 = Fan.objects.filter(device=35).distinct().values('fan_name', 'fan_status', 'fan_health')
    e1efs05 = Fan.objects.filter(device=36).distinct().values('fan_name', 'fan_status', 'fan_health')
    e1drf04 = Fan.objects.filter(device=37).distinct().values('fan_name', 'fan_status', 'fan_health')
    e1fdp05 = Fan.objects.filter(device=38).distinct().values('fan_name', 'fan_status', 'fan_health')
    e1sdp05 = Fan.objects.filter(device=39).distinct().values('fan_name', 'fan_status', 'fan_health')
    e1cs2a = Fan.objects.filter(device=40).distinct().values('fan_name', 'fan_status', 'fan_health')
    context = {'e1sim01' : e1sim01, 'e1sdr05' : e1sdr05, 'e1efs05' : e1efs05, 'e1drf04' : e1drf04, 'e1fdp05' : e1fdp05, 'e1sdp05' : e1sdp05, 'e1cs2a' : e1cs2a, 'data_device' : data_device, 'test' : test,}
    return render(request, 'sys_mon/test.html', context)