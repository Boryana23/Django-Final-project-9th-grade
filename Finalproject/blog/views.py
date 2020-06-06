from django.shortcuts import render

from blog.models import Post
# Create your views here.
def index(request):
    posts = Post.objects.all()
    dictionary = {"posts" : posts}
    return render(request, "index.html", dictionary)