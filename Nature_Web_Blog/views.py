from django.shortcuts import render, get_object_or_404
from Nature_Web_Blog.models import Post
# Create your views here.
def allpost(request):
    post = Post.objects
    return render(request,'posts.html',{'post':post})

def detail(request, Nature_Web_Blog_id):
    detail = get_object_or_404(Post,pk = Nature_Web_Blog_id)
    return render(request,'details.html',{'post':detail})
