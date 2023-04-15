from django.urls import path

from . import views

urlpatterns = [
    path("", views.starting_page, name="starting-page"),
    path("posts", views.posts, name="posts-page"),
    # posts/my-first-posts
    path("posts/<slug:slug>", views.post_detail,  name="post-detail-page"),
   # path("random", views.randomm, name="random-page")
]
