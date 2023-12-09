from django.shortcuts import render
from django.http import JsonResponse
from .models import Info

def get_terms(request):
    infos=Info.objects.all()
    data = [{'id': info.id, 'content': info.content} for info in infos]
    return JsonResponse({'infos': data})