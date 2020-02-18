# from django.shortcuts import render

from django.shortcuts import render, get_object_or_404
from .models import Post, Comment
from .forms import NewComment  # , PostCreateForm
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
# from django.views.generic import CreateView, UpdateView, DeleteView
# from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


# posts = [
#     {
#         'title': 'التدوينة الأولى',
#         'content': 'نص التدوينة الأولى كنص تجريبى',
#         'post_date': '15-3-2019',
#         'author': 'أحمد أبوعيسى'
#     },
#     {
#         'title': 'التدوينة الثانية',
#         'content': 'نص التدوينة كنص تجريبى',
#         'post_date': '19-4-2019',
#         'author': 'أحمد أبوعيسى المحترم'
#     },
#     {
#         'title': 'التدوينة الثالة',
#         'content': 'نص التدوينة كنص تجريبى',
#         'post_date': '20-3-2018',
#         'author': 'أبوعيسى أحمد'
#     },
#     {
#         'title': 'التدوينة الرابعة',
#         'content': 'نص التدوينة كنص تجريبى',
#         'post_date': '29-5-2019',
#         'author': 'أحمد السيد أبوعيسى'
#     }
# ]


def home(request):
    context = {
        'title': 'الصفحة الرئيسية',
        # 'posts': posts
        'posts': Post.objects.all()
    }
    return render(request, 'blog/index.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'من أنا'})


def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    # comments is the related_name for field ..
    comments = post.comments.filter(active=True)

    # check before save data from comment form
    if request.method == 'POST':
        comment_form = NewComment(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
            comment_form = NewComment()
    else:
        comment_form = NewComment()

    context = {
        'title': post,
        'post': post,
        'comments': comments,
        'comment_form': comment_form,
    }

    return render(request, 'blog/detail.html', context)
