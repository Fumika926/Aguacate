from django.shortcuts import render
from django.http import HttpResponse

# No sé que es esto jeje
def index(request):
    # AAAAAAAAAAAAAGRIA
    print('Soy un log de un servidor ')
    print('--Entrando al index--')
    return HttpResponse('por la chucha')