from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render

# from fairy_forest_app.models import Image
from fairy_forest_app.models import FairyForest


def fairy_forest(request):
    """Отображение Сказочного леса"""
    pages = FairyForest.objects.filter(draft=False)
    paginator = Paginator(pages, 1)

    page_number = request.GET.get('page')

    try:
        page = paginator.get_page(page_number)
    except PageNotAnInteger:
        page = paginator.get_page(1)
    except EmptyPage:
        page = paginator.get_page(paginator.num_pages)

    context = {
        'page': page
    }

    return render(request, 'fairy_forest/index.html', context=context)
