# project_1/views.py
from django.http import JsonResponse

def hello_world_view(request):
    data = {'message': 'Hello World'}
    return JsonResponse(data)
