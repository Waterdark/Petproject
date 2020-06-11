from django.http import HttpResponse
#функция отображения страници blog
def hello(request):
    return HttpResponse('<h1>Hello!</h1>')