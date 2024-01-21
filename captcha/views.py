from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    context = {
        "captcha_completed": False
    }
    return render(request, "captcha/index.html", context)


def solvecaptcha(request):
    return HttpResponse("Sussus Amogus")
