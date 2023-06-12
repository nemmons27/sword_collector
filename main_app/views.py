from django.shortcuts import render
from .models import Sword

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def swords_index(request):
    swords = Sword.objects.all()
    return render(request, 'swords/index.html', {
        'swords': swords
    })

def swords_detail(request, sword_id):
    sword = Sword.objects.get(id=sword_id)
    return render(request, 'swords/detail.html', { 'sword': sword })