from datetime import date
from urllib import request
from django.shortcuts import render, get_object_or_404

from . models import Post

# Временныые данные для постов. Потом будет из базы данных

all_posts = [
    {
        "slug": "post-01-title",
        "img": "post_01.jpg",
        "autor": "arty",
        "date": date(2022, 1, 1),
        "title": "Post Title 01",
        "excerpt": "111Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc facilisis congue lectus vitae facilisis. Suspendisse condimentum quam eu metus porta, ac suscipit risus ursus. Nunc id risus leo.",
        "content": """
            111Lorem ipsum dolor sit, amet consectetur adipisicing elit. Quo a eius cum eum explicabo iure, ex iste sed magni
            omnis, eaque voluptatibus! Ab commodi quidem libero laborum earum mollitia iste.

            Lorem ipsum dolor sit, amet consectetur adipisicing elit. Quo a eius cum eum explicabo iure, ex iste sed magni
            omnis, eaque voluptatibus! Ab commodi quidem libero laborum earum mollitia iste.

            Lorem ipsum dolor sit, amet consectetur adipisicing elit. Quo a eius cum eum explicabo iure, ex iste sed magni
            omnis, eaque voluptatibus! Ab commodi quidem libero laborum earum mollitia iste.
        """
    },
    {
        "slug": "post-02-title",
        "img": "post_02.jpg",
        "autor": "arty2",
        "date": date(2022, 1, 2),
        "title": "Post Title 02",
        "excerpt": "222Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc facilisis congue lectus vitae facilisis. Suspendisse condimentum quam eu metus porta, ac suscipit risus ursus. Nunc id risus leo.",
        "content": """
            222Lorem ipsum dolor sit, amet consectetur adipisicing elit. Quo a eius cum eum explicabo iure, ex iste sed magni
            omnis, eaque voluptatibus! Ab commodi quidem libero laborum earum mollitia iste.

            Lorem ipsum dolor sit, amet consectetur adipisicing elit. Quo a eius cum eum explicabo iure, ex iste sed magni
            omnis, eaque voluptatibus! Ab commodi quidem libero laborum earum mollitia iste.

            Lorem ipsum dolor sit, amet consectetur adipisicing elit. Quo a eius cum eum explicabo iure, ex iste sed magni
            omnis, eaque voluptatibus! Ab commodi quidem libero laborum earum mollitia iste.
        """
    },
    {
        "slug": "post-03-title",
        "img": "post_03.jpg",
        "autor": "arty3",
        "date": date(2022, 1, 3),
        "title": "Post Title 03",
        "excerpt": "333Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc facilisis congue lectus vitae facilisis. Suspendisse condimentum quam eu metus porta, ac suscipit risus ursus. Nunc id risus leo.",
        "content": """
            333Lorem ipsum dolor sit, amet consectetur adipisicing elit. Quo a eius cum eum explicabo iure, ex iste sed magni
            omnis, eaque voluptatibus! Ab commodi quidem libero laborum earum mollitia iste.

            Lorem ipsum dolor sit, amet consectetur adipisicing elit. Quo a eius cum eum explicabo iure, ex iste sed magni
            omnis, eaque voluptatibus! Ab commodi quidem libero laborum earum mollitia iste.

            Lorem ipsum dolor sit, amet consectetur adipisicing elit. Quo a eius cum eum explicabo iure, ex iste sed magni
            omnis, eaque voluptatibus! Ab commodi quidem libero laborum earum mollitia iste.
        """
    },
    {
        "slug": "post-04-title",
        "img": "post_04.jpg",
        "autor": "arty4",
        "date": date(2022, 1, 4),
        "title": "Post Title 04",
        "excerpt": "444Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc facilisis congue lectus vitae facilisis. Suspendisse condimentum quam eu metus porta, ac suscipit risus ursus. Nunc id risus leo.",
        "content": """
            444Lorem ipsum dolor sit, amet consectetur adipisicing elit. Quo a eius cum eum explicabo iure, ex iste sed magni
            omnis, eaque voluptatibus! Ab commodi quidem libero laborum earum mollitia iste.

            Lorem ipsum dolor sit, amet consectetur adipisicing elit. Quo a eius cum eum explicabo iure, ex iste sed magni
            omnis, eaque voluptatibus! Ab commodi quidem libero laborum earum mollitia iste.

            Lorem ipsum dolor sit, amet consectetur adipisicing elit. Quo a eius cum eum explicabo iure, ex iste sed magni
            omnis, eaque voluptatibus! Ab commodi quidem libero laborum earum mollitia iste.
        """
    },
    {
        "slug": "post-05-title",
        "img": "post_05.jpg",
        "autor": "arty5",
        "date": date(2022, 1, 5),
        "title": "Post Title 05",
        "excerpt": "555Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc facilisis congue lectus vitae facilisis. Suspendisse condimentum quam eu metus porta, ac suscipit risus ursus. Nunc id risus leo.",
        "content": """
            555Lorem ipsum dolor sit, amet consectetur adipisicing elit. Quo a eius cum eum explicabo iure, ex iste sed magni
            omnis, eaque voluptatibus! Ab commodi quidem libero laborum earum mollitia iste.

            Lorem ipsum dolor sit, amet consectetur adipisicing elit. Quo a eius cum eum explicabo iure, ex iste sed magni
            omnis, eaque voluptatibus! Ab commodi quidem libero laborum earum mollitia iste.

            Lorem ipsum dolor sit, amet consectetur adipisicing elit. Quo a eius cum eum explicabo iure, ex iste sed magni
            omnis, eaque voluptatibus! Ab commodi quidem libero laborum earum mollitia iste.
        """
    },
    {
        "slug": "post-06-title",
        "img": "post_06.jpg",
        "autor": "arty6",
        "date": date(2022, 1, 6),
        "title": "Post Title 06",
        "excerpt": "666Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc facilisis congue lectus vitae facilisis. Suspendisse condimentum quam eu metus porta, ac suscipit risus ursus. Nunc id risus leo.",
        "content": """
            666Lorem ipsum dolor sit, amet consectetur adipisicing elit. Quo a eius cum eum explicabo iure, ex iste sed magni
            omnis, eaque voluptatibus! Ab commodi quidem libero laborum earum mollitia iste.

            Lorem ipsum dolor sit, amet consectetur adipisicing elit. Quo a eius cum eum explicabo iure, ex iste sed magni
            omnis, eaque voluptatibus! Ab commodi quidem libero laborum earum mollitia iste.

            Lorem ipsum dolor sit, amet consectetur adipisicing elit. Quo a eius cum eum explicabo iure, ex iste sed magni
            omnis, eaque voluptatibus! Ab commodi quidem libero laborum earum mollitia iste.
        """
    }
]


# Create your views here.


def blog(request):
    # slice 3 первые элемента не влияет на производительность
    # django создаёт хитрый sql запрос, выбирающий сразу 3 записи
    # не поддерживает [:-3] но это и не нужно, order_by это делает
    latest_posts = Post.objects.all().order_by("-date")[:3]
        
    # Т.к. app прописан в INSTALLED_APPS, то папку templates (в app) не указываем, только blog
    return render(request, "blog/index.html", {
        "posts": latest_posts           # контекст для передачи в html
    })


def posts(request):
    all_posts = Post.objects.all().order_by("-date")
    return render(request, "blog/all-posts.html", {
        "all_posts": all_posts
    })

def post_detail(request, slug):
    # detail_post = Post.objects.get(slug__exact=slug)
    detail_post = get_object_or_404(Post, slug=slug)
    return render(request, "blog/post-detail.html", {
        "post": detail_post,
        "tags": detail_post.tag.all()
    })

def html_test_01(request):
    return render(request, "blog/html-test/html-test_01.html")

