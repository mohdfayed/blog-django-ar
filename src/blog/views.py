# from django.shortcuts import render

from django.shortcuts import render, get_object_or_404
from .models import Post, Comment
from .forms import NewComment, PostCreateForm
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# video 38, use class based views to create new blog
from django.views.generic import CreateView, UpdateView, DeleteView
# use these for protectin class Based View
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


def home(request):
    posts = Post.objects.all()
    paginator = Paginator(posts, 5)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_page)
    context = {
        'title': 'الصفحة الرئيسية',
        'posts': posts,
        'page': page,
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

# video 38, use class based views to create new blog ===============================================
# Use LoginRequiredMixin this way with class Based View


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    # fields = ['title', 'content']
    template_name = 'blog/post_new.html'
    form_class = PostCreateForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(UserPassesTestMixin, LoginRequiredMixin, UpdateView):
    model = Post
    template_name = 'blog/post_update.html'
    form_class = PostCreateForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # to be used by UserPassesTestMixin to verify user is the post.author
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False


class PostDeleteView(UserPassesTestMixin, LoginRequiredMixin, DeleteView):
    model = Post
    # DeleteView let it look for this file by default
    # template_name = 'blog/post_confirm_delte.html'

    # by default after delete DeleteView looks for this direction
    success_url = '/'

    # to be used by UserPassesTestMixin to verify user is the post.author
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
