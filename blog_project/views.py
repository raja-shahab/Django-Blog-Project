from django.shortcuts import render, redirect
from app.models import Post, Category, Tag

def BASE(request):
    return render(request, 'main/base.html')

def HOME(request):
    popular_posts = Post.objects.filter(section ='Popular').order_by('-id')[0:4]
    recent_posts = Post.objects.filter(section ='Recent').order_by('-id')[0:4]
    main_post = Post.objects.filter(main_post = True)
    editors_pick = Post.objects.filter(section = 'Editors Pick').order_by('-id')
    trending = Post.objects.filter(section = 'Trending').order_by('-id')
    inspiration = Post.objects.filter(section = 'Inspiration').order_by('-id')[0:2]
    latest_post = Post.objects.filter(section = 'Latest Post').order_by('-id')[0:4]

    category = Category.objects.all()
    all_sections = Post.objects.values_list('section', flat=True)
    unique_sections = set(all_sections)

    context = {
        'popular_posts': popular_posts,
        'recent_posts' : recent_posts,
        'main_post' : main_post,
        'editors_pick' : editors_pick,
        'trending' : trending,
        'inspiration' : inspiration,
        'latest_post' : latest_post,

        'category' : category,
        'unique_sections' : unique_sections

    }

    return render(request, 'main/index.html', context)

def CONTACT(request):
    return render(request, 'contact.html')


def BLOG(request):
    tags = Post.objects.prefetch_related('tag_set').all()


    context = {
        'tags' : tags
    }
    return render(request, 'single_blog.html', context)