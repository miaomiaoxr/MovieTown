import datetime
import os
from turtle import title
from unicodedata import category

from django import views
os.environ.setdefault('DJANGO_SETTINGS_MODULE','MovieTown.settings')

import django
django.setup()
from movie.models import Category,Movie

def populate():

    action_movie = [
        {
            'name': 'No Time to Die',
            'director': 'Cary Joji Fukunaga',
            'lead_actor': 'Daniel Craig',
            'description':'This is a 007 Movie',
            'pub_date':datetime.date(2017,5,17),
        }
    ]

    romantic_moive = [
        {
            'name': 'Titanic',
            'director': 'James Cameron',
            'lead_actor': 'Leonardo DiCaprio',
            'description':'This is a titanic Movie',
            'pub_date':datetime.date(1997,12,19),
        }
    ]



    cats = {
        'Action':{
            'pages':action_movie,
        },
        'Romantic':{
            'pages':romantic_moive,
        }
    }

    for cat,cat_data in cats.items():
        c = add_cat(cat)
        for p in cat_data['pages']:
            add_page(c,p['name'],p['director'],p['lead_actor'],p['description'],p['pub_date'])

    for c in Category.objects.all():
        for p in Movie.objects.filter(category=c):
            print(f'- {c}:{p}')

def add_page(cat,name,director,lead_actor,description,pub_date):
    p = Movie.objects.get_or_create(category=cat, name=name)[0]
    p.director = director
    p.lead_actor = lead_actor
    p.description = description
    p.pub_date = pub_date
    p.save()
    return p

def add_cat(name):
    c = Category.objects.get_or_create(name=name)[0]
    c.save()
    return c

if __name__ == '__main__':
    print('Starting Rango population script...')
    populate()