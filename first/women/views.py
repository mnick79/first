from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>THe my first page</h1>")

def categories(request, catid):
    def fuct(ii):
        if ii <= 1:
            return 1
        return fuct(ii - 1) * ii
    return HttpResponse(f"<h1>The my second page</h1><p>{fuct(int(catid))}</p>")


def archive(request, year):
    if int(year) < 10:
        return HttpResponse(f'Вывод {fuct(int(year))}')
    return HttpResponse("Error input")

def boots(request, method=['GET']):
    if request.GET:
        return HttpResponse(''.join([i+" = +j+'<br>' for i,j in request.GET.items()]))
    return HttpResponse("Ошибка ввода!")