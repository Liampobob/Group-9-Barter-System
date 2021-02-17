from django.http import HttpResponse, JsonResponse


def test(request):
    return HttpResponse("Hello, world.")

def status(request):
    return JsonResponse({'status_code':'400', 'status':'Probably Working'})
