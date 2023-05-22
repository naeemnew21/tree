from django.shortcuts import render
from .models import Person, Family, Hist, Log_Info
from django.contrib.gis.geoip2 import GeoIP2
from django.contrib.auth.decorators import user_passes_test



def get_info(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')

    device_type = ""
    browser_type = ""
    browser_version = ""
    os_type = ""
    os_version = ""
    if request.user_agent.is_mobile:
        device_type = "Mobile"
    if request.user_agent.is_tablet:
        device_type = "Tablet"
    if request.user_agent.is_pc:
        device_type = "PC"

    browser_type = request.user_agent.browser.family
    browser_version = request.user_agent.browser.version_string
    os_type = request.user_agent.os.family
    os_version = request.user_agent.os.version_string


    g = GeoIP2()
    location = g.city(ip)

    location_country = location["country_name"]
    location_city = location["city"]

    context = {
        "ip": ip,
        "device_type": device_type,
        "browser_type": browser_type,
        "browser_version": browser_version,
        "os_type":os_type,
        "os_version":os_version,
        "location_country": location_country,
        "location_city": location_city
    }
    date = Hist.objects.create()
    log, created = Log_Info.objects.get_or_create(**context)
    log.history.add(date)
    return context


def index(request):
    try:
        get_info(request)
    except:
        pass
    qs = Person.objects.all()
    if qs:
        ctx = {'root' : qs[0]}
    else:
        ctx = {'root' : ''}
    if request.user.is_authenticated and request.user.is_superuser:
        return render(request, 'edit-tree.html', context=ctx)
    return render(request, 'index.html', context=ctx)



def naeem(request):
    try:
        get_info(request)
    except:
        pass
    qs = Family.objects.all()
    if qs:
        ctx = {'root' : qs[0]}
    else:
        ctx = {'root' : ''}
    if request.user.is_authenticated and request.user.is_superuser:
        return render(request, 'naeem-edit.html', context=ctx)
    return render(request, 'naeem.html', context=ctx)


def is_admin(user):
    return user.is_authenticated and user.is_superuser and user.username == "admin"



@user_passes_test(is_admin, login_url='/admin' )
def log_history(request):
    ctx = dict()
    try:
        info = get_info(request)
    except:
        info = dict()
    qs = Log_Info.objects.all()
    ctx['logs'] = qs
    ctx.update(info)
    return render(request, 'log.html', ctx)

