from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>THe my first page</h1>")

def categories(request, catid):
    return HttpResponse(f"<h1>The my second page</h1><p>{catid*2}</p>")

def archive(request, year):
    if int(year) > 2021:
        return HttpResponse(f'Вывод {year}')
    return HttpResponse(f'PageNotFound!')

def boots(request, method=['GET']):
    print(f'" ".join([a+"="+b+"\n" for a,b in request.GET.items()])')
    return HttpResponse(f'{"".join([a+"="+b+"  " for a,b in request.GET.items()])}')