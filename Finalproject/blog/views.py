from django.shortcuts import get_object_or_404, render

from blog.models import Post


# Create your views here.
def handle_uploaded_file(f):
    with open("media/" + f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


def index(request):
        posts = Post.objects.all()
        dictionary = {"posts" : posts}
        return render(request, "index.html", dictionary)

def create(request):
    if request.method == "POST":
        print(request.FILES)
        object1 = Post(title = request.POST.get("title"),
                    text = request.POST.get("text"),
                    image = request.FILES.get("image").name)
        object1.save()
        handle_uploaded_file(request.FILES["image"])
        return render(request, "success.html")
    return render(request, "create.html")




def detail(request, post_id):
    post = get_object_or_404(Post, pk = post_id)
    context = {"post": post}
    return render(request, "details.html", context)