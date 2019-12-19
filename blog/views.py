from django.shortcuts import render
from . models import Comment, Category, Post
from .forms import CommentForm

def blog_index(request):
    posts = Post.objects.all().order_by('-creted_on')
    context = {
        "posts":posts
    }
    return render(request, 'blog.html', context)


def blog_category(request, category):
    posts = Post.objects.filter(categories_name_contains=category).order_by('-created_on')
    context = {'category':category,
               'posts':posts
               
               }
    
    return render(request, 'blog_category.html', context)

def blog_detail(request, pk):
    post = Post.objects.get(pk=pk)
    forms = CommentForm()
    if request.form == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author = form.cleaned_data["author"],
                body = form.cleaned_data["body"],
                post = post
            )
            comment.save()
    
    comments = Comment.objects.filter(post=post)
    context = {
        "post": post,
        "comments": comments,
        "form":form,
    }

    return render(request, "blog_detail.html", context)