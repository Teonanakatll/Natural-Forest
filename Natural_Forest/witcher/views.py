from django.shortcuts import render

from witcher.models import Witcher


def witcher(request):
    slides = Witcher.objects.filter(draft=False)
    return render(request, 'witcher/witcher.html', locals())
