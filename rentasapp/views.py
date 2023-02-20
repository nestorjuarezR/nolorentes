from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    "Vista para mostar pagina principal"
    return render(request, "rentasapp/index.html")