"""MovieTown URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path,include
from movie import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('search/', views.search, name='searchpage'),
    path('movie/', include('movie.urls')),
    path('admin/', admin.site.urls),
    path('accounts/',include('registration.backends.simple.urls')),
    path('accounts/user_profile/',views.user_profile,name='user_profile'),
    path('accounts/user_profile/<int:pk>',views.delete_comments_user_profile,name='comment_delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)