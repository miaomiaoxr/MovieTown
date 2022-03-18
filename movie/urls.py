from django.urls import URLPattern, path
from movie import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'movie'

urlpatterns = [
    path('', views.index, name='index'),
    path('category/<slug:category_name_slug>/', views.show_category, name='show_category'),
    path('<slug:movie_name_slug>/', views.moviepage, name ='moviepage'),
]
