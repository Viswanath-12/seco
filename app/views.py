from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def rohit(request):
    return HttpResponse('Malayali chetta')


def row(request):
    return render(request,'row.html')