from django.contrib import admin
from django.utils.safestring import mark_safe

from book.models import Genre, Book, Review, Video


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ["name", "photo"]


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = [
        "pk",
        "genre",
        "title",
        "writer",
        "publisher",
        "image",
        "price",
        "desc",
    ]

    # 적절히 썸네일처리해주면, 페이지가 좀 더 빨리 뜨고, 서버 부담도 줄어든다.
    def image(self, book: Book):
        # 아래 url 수정하기
        html = f'<img src="{book.image.url}" style="width: 100px;" />'
        return mark_safe(html)

    image.short_description = "책 표지 이미지"


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ["book", "video_title", "youtube_url"]

    def youtube_url(self, video: Video) -> str:
        html = f'<a href="{video.youtube_url}" target="_blank"> 북 트레일러 보기</a>'
        return mark_safe(html)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    pass
