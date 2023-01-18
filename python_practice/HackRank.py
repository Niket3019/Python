from . import HttpResponse
def index(request):
    file = open("1.txt")
    return HttpResponse(file.read())