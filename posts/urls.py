''' Posts urls'''


#Django

from django.urls import path

#Models

from posts import views


urlpatterns =[
    path(
        route= 'posts/latest_posts/',
        view = views.latest_posts,
        name="latest_posts"
    ),
]