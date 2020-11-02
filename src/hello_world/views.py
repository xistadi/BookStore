from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world!<br> <a href='/references'>Перейти к словарям</a><br>"
                        "<a href='/books'>Перейти к книгам</a><br>")
