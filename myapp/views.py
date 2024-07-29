from django.http import HttpResponse

def hello_world(request):
    return HttpResponse("<h1>Hello, Yuliia!</h1>")