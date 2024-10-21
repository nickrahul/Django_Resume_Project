from django.shortcuts import render

# Create your views here.


def skills(request):
    return render (request, 'skills/skill.html',{'skills':'active'})