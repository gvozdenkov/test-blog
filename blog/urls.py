from unicodedata import name
from django.urls import path

# импортировать из текущей директории файл views с отображениями адресов
from . import views

# urls приложения
urlpatterns = [
    path('', views.blog, name="blog-home"),
    path('posts', views.posts, name="posts-page"),
    
    # slug - любое переменное текстовое значение, например posts/my-first-post
    path('posts/<slug:slug>', views.post_detail, name="post-detail-page"),

    # адрес для тестов голого html
    path('html-test-01', views.html_test_01, name="html-test")
]
