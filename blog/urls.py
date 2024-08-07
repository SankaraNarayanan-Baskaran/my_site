from django.urls import path
from . import views
urlpatterns = [
    path("", views.StartingPageView.as_view(), name="starting-page"),
    path("posts", views.PostsView.as_view(), name="posts-page"),
    path("posts/<slug:slug>", views.PostDetailView.as_view(),
         name="post-detail-page") , # /posts/my-first-post
    path("read-later",views.ReadLater.as_view(),name="read-later")
]
