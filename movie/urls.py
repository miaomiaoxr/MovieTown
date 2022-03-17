from django.urls import URLPattern, path
from movie import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'movie'

urlpatterns = [
    path('', views.index, name='index'),
    path('<slug:movie_name_slug>/',views.moviepage,name="moviepage"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)