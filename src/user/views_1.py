from django.shortcuts import render, redirect
from .forms import UserCreationForm, LoginForm, UserUpdateForm, ProfileUpdateForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from blog.models import Post
from user.models import Profile
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            # username = form.cleaned_data['username']
            new_user.set_password(form.cleaned_data['password1'])
            new_user.save()
            # messages.success(
            #    request, 'تهانينا {} لقد تمت عملية التسجيل بنجاح.'.format(username))
            messages.success(
                request, f'تهانينا {new_user} لقد تمت عملية التسجيل بنجاح.')
            # return redirect('home')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'user/register.html', {
        'title': 'التسجيل',
        'form': form,
    })


def login_user(request):
    if request.method == 'POST':
        # form = LoginForm()  # Removed to use html form directly
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # return redirect('home')
            return redirect('profile')
        else:
            messages.warning(
                request, 'هناك خطأ في اسم المستخدم أو كلمة المرور.')
    # else:
        # form = LoginForm()  # Removed to use html form directly
    return render(request, 'user/login.html', {
        'title': 'تسجيل الدخول',
        # 'form': form,  # Removed to use html form directly
    })


def logout_user(request):
    logout(request)
    return render(request, 'user/logout.html', {
        'title': 'تسجيل الخروج'
    })


@login_required(login_url='login')
def profile(request):
    posts = Post.objects.filter(author=request.user)
    post_list = Post.objects.filter(author=request.user)
    paginator = Paginator(post_list, 5)
    page = request.GET.get('page')
    try:
        post_list = paginator.page(page)
    except PageNotAnInteger:
        post_list = paginator.page(1)
    except EmptyPage:
        post_list = paginator.page(paginator.num_page)
    # Mine Start
    print(request.user)
    print(request.user.id)
    idx = request.user.id
    image_x = Profile.objects.get(pk=idx)
    image_x = image_x.image.url
    print(image_x)
    # End Mine
    # print(post_list)
    return render(request, 'user/profile.html',
                  {
                      'title': 'الملف الشخصى',
                      'posts': posts,
                      'post_list': post_list,
                      'page': page,
                      'image_x': image_x,
                  })


@login_required(login_url='login')
def profile_update(request):
    user_form = UserUpdateForm()
    profile_form = ProfileUpdateForm()

    #     if request.method == 'POST':
    #         user_form = UserUpdateForm(request.POST, instance=request.user)
    #         profile_form = ProfileUpdateForm(
    #             request.POST, request.FILES, instance=request.user.profile)
    #         if user_form.is_valid and profile_form.is_valid:
    #             user_form.save()
    #             profile_form.save()
    #             messages.success(
    #                 request, 'تم تحديث الملف الشخصي.')
    #             return redirect('profile')
    #     else:
    #         user_form = UserUpdateForm(instance=request.user)
    #         profile_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'title': 'تعديل الملف الشخصي',
        'user_form': user_form,
        'profile_form': profile_form,
    }

    return render(request, 'user/profile_update.html', context)
