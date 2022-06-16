from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from posts.models import Post

# Create your views here.
@login_required
def latest_posts(request):
    posts = Post.objects.get(classification= 'plastic')
    return render(
        request,
        'posts/latest_posts.html',
        {
            'posts': posts
        }
    )
