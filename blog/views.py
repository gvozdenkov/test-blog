from django.shortcuts import render

# Create your views here.


def blog(request):
    # отобразить этот темплейт.
    # Т.к. app прописан в INSTALLED_APPS, то папку templates (в app) не указываем, только blog
    return render(request, "blog/index.html")


def posts(request):
    pass


def post_detail(request):
    pass
