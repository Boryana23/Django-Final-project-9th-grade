from django.shortcuts import render

from blog.models import Post
# Create your views here.
def index(request):
    posts = Post.objects.all()
    dictionary = {"posts" : posts}
    return render(request, "index.html", dictionary)

def create(request):
    if request.method == "POST":
        obj = Post(title = request.POST.get("title"),
                    text = request.POST.get("text"),
                    image = request.POST.get("image"))
        obj.save()
        return render(request, "success.html")
    return render(request, "create.html")