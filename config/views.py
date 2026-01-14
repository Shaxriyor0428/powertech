from django.http import HttpResponse

def index_view(request):
    html_message = "<h1>Hello World</h1>"
    return HttpResponse(html_message)
