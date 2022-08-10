from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from posts.models import Post

# Create your views here.
def latest_posts(request):
    if request.user.id != None:
        profile = request.user.profile
    else:
        profile = ""

    posts = Post.objects.get(classification= 'plastic')

    context = {
        'profile': profile,
        'posts': posts
    }

    return render(request,'posts/latest_posts.html',context)
