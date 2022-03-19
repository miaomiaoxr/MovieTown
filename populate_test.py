import datetime 
import os

from django import views
os.environ.setdefault('DJANGO_SETTINGS_MODULE','MovieTown.settings')

import django
django.setup()
from movie.models import Category,Movie


c = Category.objects.get_or_create(name='action')[0]
p = Movie.objects.create(category=c,name='1917',pub_date = datetime.date(2019,12,4))
p.director = 'Sam Mendes'
p.lead_actor = 'Dean-Charles Chapman'
p.description = 'April 6th, 1917.'
p.movie_image = 'movie_image/1917.jpg'
p.save()