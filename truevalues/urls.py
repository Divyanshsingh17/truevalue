"""truevalues URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from accounts import views
from base import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index, name = 'home'),
    path('about/',views.about, name = 'about'),
    path('agents/',views.agents, name = 'agents'),
    path('user_profile/',views.user_profile_view, name = 'user_profile'),
    path('edit_profile/',views.edit_profile, name = 'editprofile'),
    path('blog/',views.blogs, name = 'blog'),
    path('blog/<int:pk>/',views.blogdetail, name = 'blogdetail'),
    path('contact/',views.contact, name = 'contact'),
    path('accounts/',include('accounts.urls')),
    path('cars/',include('cars.urls')),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'), name='password_reset_done'),
    # path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="accounts/password_reset_confirm.html"), name='password_reset_confirm'),
    # path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'), name='password_reset_complete'),      
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
