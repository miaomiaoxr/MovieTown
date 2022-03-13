from django.contrib import admin
from movie.models import Movie,Category,User,Comment
# Register your models here.

admin.site.register(Category)
admin.site.register(Movie)
admin.site.register(Comment)