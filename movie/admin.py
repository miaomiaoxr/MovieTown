from django.contrib import admin
from movie.models import Movie,Category
# Register your models here.

admin.site.register(Category)
admin.site.register(Movie)