from django.contrib.contenttypes.models import ContentType
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render

from creative_scroll.models import GenericGalleryItem, Gallery, TextItem, ImageItem, Canvas


def creative_scroll(request):
    lst = Canvas.objects.all()

    paginator = Paginator(lst, 1)
    page_number = request.GET.get('page')

    try:
        page_obj = paginator.get_page(page_number)
    except EmptyPage:
        page_obj = paginator.get_page(1)
    except PageNotAnInteger:
        page_obj = paginator.get_page(paginator.num_pages)

    left_gallery = page_obj[0].left_gallery
    right_gallery = page_obj[0].right_gallery

    l_items = list(GenericGalleryItem.objects.filter(gallery=left_gallery).select_related('content_type'))
    l_items.sort(key=lambda x: x.content_object.number)

    r_items = list(GenericGalleryItem.objects.filter(gallery=right_gallery).select_related('content_type'))
    r_items.sort(key=lambda x: x.content_object.number)
    return render(request, 'creative_scroll/creative_scroll.html', {'l_items': l_items, 'r_items': r_items, 'page_obj': page_obj})
