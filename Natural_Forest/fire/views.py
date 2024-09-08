from django.shortcuts import render

from fire.models import Fire


def fire(request):
    fire = Fire.objects.filter(draft=False)[0]
    return render(request, 'fire/fire.html', locals())
