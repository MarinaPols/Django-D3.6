from django.contrib import admin
#D3
from .models import Author, Category, Post, PostCategory, Comment

admin.site.register(Author)
admin.site.register(Category)
admin.site.register(PostCategory)
admin.site.register(Post)
admin.site.register(Comment)
# Register your models here.