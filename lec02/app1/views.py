from django.http import HttpResponse

def index(request):
    return HttpResponse("هذه صفحة تطبيق 1")
