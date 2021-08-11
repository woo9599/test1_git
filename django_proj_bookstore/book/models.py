from django.core.checks import messages
import book
from django.db import models
from django.template.loader import render_to_string
from django.db.models.deletion import CASCADE
from django.urls import reverse
from django.contrib.auth.models import User


class Genre(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    photo = models.ImageField()

    def __str__(self):
        return self.name


class Book(models.Model):
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    writer = models.CharField(max_length=100)
    publisher = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    desc = models.TextField()
    image = models.ImageField()

    def __str__(self):
        return self.title

    def get_absolute_url(self) -> str:
        # return f"/movie/movies/{self.pk}/" #하드코딩
        url = reverse("book_detail", args=[self.pk])
        # url = reverse('movie_detail',kwargs=["pk":self.pk])
        return url


class Video(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    video_title = models.CharField(max_length=100)
    youtube_url = models.URLField()

    @property
    def youtube_id(self):
        # https://www.youtube.com/watch?v=xyfozmk1SxQ
        if "v=" in self.youtube_url:
            return self.youtube_url.split("v=")[1]
        return None

    @property
    def youtube_embed_html(self):
        if self.youtube_id:
            return render_to_string(
                "book/_youtube_embed.html",
                {
                    "youtube_id": self.youtube_id,
                },
            )
        return None


class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    message = models.TextField()

    def __str__(self) -> str:
        return self.message


# Create your models here.
