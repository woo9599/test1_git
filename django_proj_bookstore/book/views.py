from django.shortcuts import redirect, render, resolve_url
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse
from book.forms import ReviewForm
from book.models import Genre, Book, Review, Video


# genre list
# 메인 페이지 디폴트 값
def genre_list(request):
    qs = Genre.objects.all()
    return render(
        request,
        "book/genre_list.html",
        {
            "genre_list": qs,
        },
    )


# genre detail
# 책 리스트 시각화
def genre_detail(request, pk):
    genre = Genre.objects.get(pk=pk)

    return render(
        request,
        "book/genre_detail.html",
        {
            "genre": genre,
        },
    )


# book list
#
def book_list(request):
    qs = Book.objects.all()
    return render(
        request,
        "book/book_list.html",
        {
            "book_list": qs,
        },
    )


# book detail + review 쓰기
def book_detail(request, pk):
    book = Book.objects.get(pk=pk)
    message_list = book.review_set.all()
    return render(
        request,
        "book/book_detail.html",
        {
            "book": book,
            "message_list": message_list,
        },
    )


def review_new(request: HttpRequest, post_pk: int) -> HttpResponse:
    post = Book.objects.get(pk=post_pk)
    if request.method == "POST":
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.book = post
            comment.save()
            return redirect(f"/book/{post_pk}/book/")
    else:
        form = ReviewForm()

    return render(
        request,
        "book/review_form.html",
        {
            "form": form,
        },
    )


def review_edit(request: HttpRequest, post_pk: int, pk: int) -> HttpResponse:
    comment = Review.objects.get(pk=pk)
    if request.method == "POST":
        form = ReviewForm(request.POST, request.FILES, instance=comment)
        if form.is_valid():
            comment = form.save()
            return redirect(f"/book/{post_pk}/book/")
    else:
        form = ReviewForm(instance=comment)

    return render(
        request,
        "book/review_form.html",
        {
            "form": form,
        },
    )


def review_delete(request: HttpRequest, post_pk: int, pk: int) -> HttpResponse:
    comment = Review.objects.get(pk=pk)
    if request.method == "POST":
        comment.delete()  # DB에 즉시 DELTE 쿼리를 전달
        return redirect(f"/book/{post_pk}/book/")

    return render(
        request,
        "book/review_confirm_delete.html",
        {
            "comment": comment,
        },
    )


# 이 응답에서 페이지 전체를 그릴 것인지? 혹은 실제 컨텐츠만 그릴 것인지를 결정.
