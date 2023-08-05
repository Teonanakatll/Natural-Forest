from django.shortcuts import render

def fairy_forest(request):
    """Отображение Сказочного леса"""
    return render(request, 'fairy_forest/index.html')
