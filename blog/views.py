from django.shortcuts import render

# Create your views here.

from .models import Post

def index(request):

    posts = Post.objects.all()
    print(posts)

    context = {
        'title' : 'blog',
        'heading' : 'blog di mywebsite',
        'posts' : posts,
    }
    
    return render(request,'blog/index.html',context)