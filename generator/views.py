from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def home(request):
    return render(request, 'generator/home.html', {'password': 'aksjhgah78nbagf!@'})

def password(request):
    thePassword = generatePassword(request)
    return render(request, 'generator/password.html', {'password':thePassword})

def generatePassword(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('number'):
        characters.extend(list('1234567890'))

    if request.GET.get('specialcharacter'):
        characters.extend(list('~!@#$%^&*'))

    length = int(request.GET.get('length', 8))

    thePassword = ''
    for x in range(length):
        thePassword += random.choice(characters)

    return thePassword
