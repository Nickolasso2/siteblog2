from django.shortcuts import render

from .models import Journey

def show_journey(request):
    return render(request, "menu/menu.html", {'places': Journey.objects.all()})
