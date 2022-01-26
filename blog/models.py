from distutils import text_file
from django.db import models
from django.forms import CharField, DateField, URLField
from tabnanny import verbose
import uuid

# Create your models here.

class Tag(models.Model):
    caption = models.CharField(max_length=20)

    def __str__(self):
        return self.caption
    

class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name()
    

class Post(models.Model):
    title = models.CharField(max_length=40)
    excerpt = models.CharField(max_length=200)
    img = models.CharField(max_length=40)
    date = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True)        #unique=true автоматом создаёт индекс
    content = models.TextField()

    author = models.ForeignKey(Author, null=True, on_delete=models.SET_NULL, related_name="posts")
    tag = models.ManyToManyField("blog.Tag")


    def __str__(self):
        return f"{self.title} ({self.date})"

    class Meta:
        verbose_name_plural = "Posts"

