from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404

from forest_app.models import NaturalForest


def index(request):
    return render(request, 'forest_app/index.html')

def forest(request):
    pages = NaturalForest.objects.filter(draft=False)

    paginator = Paginator(pages, 1)
    page_number = request.GET.get('page')
    try:
        page = paginator.get_page(page_number)
    except PageNotAnInteger:
        page = paginator.get_page(1)
    except EmptyPage:
        page = paginator.get_page(paginator.num_pages)

    return render(request, 'forest_app/natural.html', locals())
