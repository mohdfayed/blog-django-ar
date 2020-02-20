from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('register/', views.register, name='register'),

    # 27 crispy
    # path('login/', LoginView.as_view(template_name='user/login.html'), name='login'),
    # path('login/', LogoutView.as_view(template_name='user/logout.html'), name='logout'),

    # 28 using forms.py (LoginForm) importing authenticate, login, logout
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),

    # profile
    path('profile/', views.profile, name='profile'),
    path('profile_update/', views.profile_update, name='profile_update'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
