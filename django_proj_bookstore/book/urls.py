from django.urls import path

from book import views

urlpatterns = [
    path("", views.genre_list, name="genre_list"),
    path("<int:pk>/", views.genre_detail, name="genre_detail"),
    path("<int:pk>/book/", views.book_detail, name="book_detail"),
    path("<int:post_pk>/book/reviews/new/", views.review_new, name="review_new"),
    path(
        "<int:post_pk>/book/<int:pk>/edit/",
        views.review_edit,
        name="review_edit",
    ),
    path(
        "<int:post_pk>/book/<int:pk>/delete/",
        views.review_delete,
        name="review_delete",
    ),
]
