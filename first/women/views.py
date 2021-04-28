from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseServerError


def fuct(ii):
    if ii <= 1:
        return 1
    return fuct(ii - 1) * ii


def index(request):
    return HttpResponse("<h1>THe my first page</h1>")


def categories(request, catid):
    return HttpResponse(f"<h1>The my second page</h1><p>{fuct(int(catid))}</p>")


def archive(request, year):
    if int(year) < 15:
        return HttpResponse(f'Вывод {fuct(int(year))}')
    else:
        return redirect('/', permanent=True)


def boots(request, method=['GET']):
    if request.GET:
        return HttpResponse(''.join([i + " = " + j + '<br>' for i, j in request.GET.items() if j != '12']))
    return HttpResponse("Ошибка ввода!")


def PageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


def Error_server(request):
    return HttpResponseServerError("Непонятная ошибка сервера")
