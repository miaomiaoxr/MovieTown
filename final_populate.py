import datetime 
import os

from django import views
os.environ.setdefault('DJANGO_SETTINGS_MODULE','MovieTown.settings')

import django
django.setup()
from movie.models import Category,Movie,User,Comment

def populate():


    action_movie = [
        {
            'name': '1917',
            'director': 'Sam Mendes',
            'lead_actor': 'Dean-Charles Chapman',
            'description':'April 6th, 1917. As an infantry battalion assembles to wage war deep in enemy territory, two soldiers are assigned to race against time and deliver a message that will stop 1,600 men from walking straight into a deadly trap.',
            'movie_image':'movie_image/1917.jpg',
            'pub_date':datetime.date(2019,12,4),
        },
        {
            'name': 'Thuppakki',
            'director': 'A.R. Murugadoss',
            'lead_actor': 'Thalapathy Vijay',
            'description':'An army captain is on a mission to track down and destroy a terrorist gang and deactivate the sleeper cells under its command.',
            'movie_image':'movie_image/Thuppakki.jpg',
            'pub_date':datetime.date(2012,12,13),
        },
        {
            'name': 'Fight Club',
            'director': 'David Fincher',
            'lead_actor': 'Brad Pitt',
            'description':'An insomniac office worker and a devil-may-care soap maker form an underground fight club that evolves into much more.',
            'movie_image':'movie_image/fight_club.jpg',
            'pub_date':datetime.date(1999,10,15),
        },
        {
            'name': 'Kill Bill: Vol. 1',
            'director': 'Quentin Tarantino',
            'lead_actor': 'Uma Thurman',
            'description':'After awakening from a four-year coma, a former assassin wreaks vengeance on the team of assassins who betrayed her.',
            'movie_image':'movie_image/kill_bill_v1.jpg',
            'pub_date':datetime.date(2003,10,10),
        },
        {
            'name': 'tenet',
            'director': 'Christopher Nolan',
            'lead_actor': 'John David Washington',
            'description':'In a twilight world of international espionage, an unnamed CIA operative, known as The Protagonist, is recruited by a mysterious organization called Tenet to participate in a global assignment that unfolds beyond real time. The mission: prevent Andrei Sator, a renegade Russian oligarch with precognition abilities, from starting World War III. The Protagonist will soon master the art of "time inversion" as a way of countering the threat that is to come.',
            'movie_image':'movie_image/tenet.jpg',
            'pub_date':datetime.date(2020,8,26),
        },
        {
            'name': 'no time to die',
            'director': 'Cary Joji Fukunaga',
            'lead_actor': 'Daniel Craig',
            'description':'James Bond has left active service. His peace is short-lived when Felix Leiter, an old friend from the CIA, turns up asking for help, leading Bond onto the trail of a mysterious villain armed with dangerous new technology.',
            'movie_image':'movie_image/no_time_to_die.jpg',
            'pub_date':datetime.date(2021,9,28),
        },
        {
            'name': 'Resident Evil: Welcome to Raccoon City',
            'director': 'Johannes Roberts',
            'lead_actor': 'Kaya Scodelario',
            'description':'Set in 1998, this origin story explores the secrets of the mysterious Spencer Mansion and the ill-fated Raccoon City.',
            'movie_image':'movie_image/Resident Evil Welcome to Raccoon City.jpg',
            'pub_date':datetime.date(2021,11,19),
        },
        {
            'name': 'uncharted',
            'director': 'Ruben Fleischer',
            'lead_actor': 'Tom Holland',
            'description':'Street-smart Nathan Drake is recruited by seasoned treasure hunter Victor "Sully" Sullivan to recover a fortune amassed by Ferdinand Magellan, and lost 500 years ago by the House of Moncada.',
            'movie_image':'movie_image/uncharted.jpg',
            'pub_date':datetime.date(2022,2,7),
        },
        {
            'name': 'The Lord of the Rings: The Fellowship of the Ring',
            'director': 'Peter Jackson',
            'lead_actor': 'Elijah Wood',
            'description':'Bilbo Baggins is a Hobbit in his 100s, living in his homeland of the Shire, adventurous by nature.',
            'movie_image':'movie_image/lord_of_rings1.jpg',
            'pub_date':datetime.date(2001,12,19),
        },
        {
            'name': 'The Lord of the Rings: The Two Towers',
            'director': 'Peter Jackson',
            'lead_actor': 'Elijah Wood',
            'description':'The film follows Frodo and Sam, Hobbits, as they continue their quest to destroy the Ring on Mordor Mountain',
            'movie_image':'movie_image/lord_of_rings2.jpg',
            'pub_date':datetime.date(2002,12,18),
        },
        {
            'name': 'The Lord of the Rings: The Return of the King',
            'director': 'Peter Jackson',
            'lead_actor': 'Elijah Wood',
            'description':'The beast army is pressing in and the battle between darkness and light is coming to a head.',
            'movie_image':'movie_image/lord_of_rings3.jpg',
            'pub_date':datetime.date(2003,12,17),
        },
        {
            'name': 'Edge of Tomorrow',
            'director': 'Doug Liman',
            'lead_actor': 'Tom Cruise',
            'description':'In the near future, a group of alien races, unmatched by any human army, are constantly attacking the Earth.',
            'movie_image':'movie_image/edge_of_tomorrow.jpg',
            'pub_date':datetime.date(2014,6,6),
        },
        {
            'name': 'The Matrix',
            'director': 'Andrew Paul Wachowski',
            'lead_actor': 'Keanu Reeves',
            'description':'In the not-too-distant future, cyber hacker Neo (Keanu Reeves) has doubts about this seemingly normal real world. He meets the hacker Trinity (played by Kelly Ann Moss) and meets Morpheus (played by Lawrence Fishburne), the leader of the hacker organization. Morpheus told him that the real world is actually controlled by a computer artificial intelligence system called "matrix", people are like animals they raise, without freedom and thought, and Neo is the saviour who can save mankind. ',
            'movie_image':'movie_image/the_matrix.jpg',
            'pub_date':datetime.date(1999,3,31),
        },

        {
            'name': 'Ant-Man',
            'director': 'Peyton Reed',
            'lead_actor': 'Paul Rudd',
            'description':'Former engineer Scott (Paul Rudd) went to prison for robbing the rich to help the poor. After he was released from prison, he embarked on the road of theft in order to fight for the right to visit his daughter. Unexpectedly, an accidental theft made him become a new generation of "ant-man", and the old ant-man Dr Hank Pym (Michael Douglas) became his mentor, but Dr Pym\'s daughter Hope (played by Michael Douglas) became his mentor. Evangeline Lilly (Evangeline Lilly) is not optimistic about him. But the crisis is imminent, in order to deal with the powerful enemy to save the world, Scott had to call his group of friends to help him complete an impossible task. And the success of the mission is also the key for Scott to save his daughter. Whether Diaosi can counterattack depends on the last blow',
            'movie_image':'movie_image/ant_man.jpg',
            'pub_date':datetime.date(2017,7,17),
        },
    ]

    romance_movie = [
        {
            'name': 'Roman Holiday',
            'director': 'Willi Wyler',
            'lead_actor': 'Audrey Hepburn',
            'description':'A one-day romance between a princess and an American journalist in Rome, Italy.',
            'movie_image':'movie_image/roman_holiday.jpg',
            'pub_date':datetime.date(1953,8,20),
        },
        {
            'name': 'Gone with the Wind',
            'director': 'Victor Fleming',
            'lead_actor': 'Vivien Leigh',
            'description':"'On the eve of the American Civil War, the daughter of Scarlett (Vivien Leigh) of Tara Manor, a southern farm, fell in love with Ashley (Leslie Howard), the son of another farmer, and was rejected. In revenge, she married the man she didn't love, Charles, the younger brother of Ashley's wife Melanie (Olivia de Havilland).During the war, Scarlett became a widow, lost her mother, and took on the burden of life. She was no longer the young lady she was. · Clark Gable Gable ornaments). However, despite the hardships of life, Scarletts feelings for Ashley have not changed. The death of Ashley's wife Melanie gave Scarlett a chance to love her husband, Rhett, and Ashley, whom she has longed for many years? What a different tomorrow will Scarlett give herself'",
            'movie_image':'movie_image/gone_with_the_wind.jpg',
            'pub_date':datetime.date(1939,12,15),
        },
    ]

    horror_movie = [
        {
            'name': 'The Silence of the Lambs',
            'director': 'Jonathan Demme',
            'lead_actor': 'Jodie Foster',
            'description':"FBI Academy cadet Clarice M. Starling (Jody Foster) is assigned by Jack Crawford (Scott Glenn) of the Behavioral Sciences Unit to visit incarcerated psychiatrist Hannibal Lecter at Baltimore State Law Hospital (played by Anthony Hopkins). Lecter asks for a transfer to a better federal agency, away from his tormentor, Dr Frederick Chilton (Anthony Heard), and offers to provide psychoanalysis of the ongoing serial killer Buffalo Bill (Ted Levine).",
           'movie_image':'movie_image/the_slience_of_the_lambs.jpg',
           'pub_date':datetime.date(1991,2,14),
        }
    ]

    other_movie = [
        {
            'name': 'Warai no daigaku',
            'director': 'Mamoru Hoshi',
            'lead_actor': 'Kôji Yakusho',
            'description':'In pre-war Japan, a government censor tries to make the writer for a theater troupe alter his comedic script. As they work with and against each other, the script ends up developing in unexpected ways.',
            'movie_image':'movie_image/warai_no_daigaku.jpg',
            'pub_date':datetime.date(2004,10,30),
        },
        {
            'name': 'The Shawshank Redemption',
            'director': 'Frank Darabont',
            'lead_actor': 'Tim Robbins',
            'description':'Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.',
            'movie_image':'movie_image/The Shawshank Redemption.jpg',
            'pub_date':datetime.date(1994,9,10),
        },
        {
            'name': 'The Truman Show',
            'director': 'Peter Weir',
            'lead_actor': 'Jim Carrey',
            'description':"Truman (Jim Carrey) is a very ordinary person, except for some strange experiences - the sudden disappearance of his first love girlfriend and his drowning father suddenly appear in front of him, he and absolutely Most American men in their 30s are no different. It made him feel lost. He has also tried to leave the place where he has lived for many years, but it is always impossible for him to do so for various reasons. Until one day, he suddenly realized that he seemed to be being followed, no matter where he went or what he did. This feeling is getting stronger and stronger. Truman decided to flee the place where he had lived for more than 30 years at all costs to find his first love. But he found that he could not escape no matter what. The truth is cruel",
            'movie_image':'movie_image/the_truman_show.jpg',
            'pub_date':datetime.date(1998,6,15),
        }
    ]

    cats = {
        'Action':{
            'movies':action_movie,
        },
        'Romantic':{
            'movies':romance_movie,
        },
        'Horror':{
            'movies':horror_movie,
        },
        'Other':{
            'movies':other_movie,
        }
    }

    users = [
        {
            'username':'Tom',
            'password':'gsdyu212@!!#!',
            'is_superuser':False,
            'is_staff':False
        },
        {
            'username':'John',
            'password':'ashd#@@!#!',
            'is_superuser':False,
            'is_staff':False
        },
        {
            'username':'Root',
            'password':'gsdg6863@$@#!',
            'is_superuser':True,
            'is_staff':True
        },
    ]

    comment = [
        {
            'text':'This is a very good film with a great plot and very well drawn characters',
            'liked_flag':True
        },
        {
            'text':'This film is right up my alley',
            'liked_flag':True
        },
        {
            'text':'This movie sucks, I don\'t really recommend this movie',
            'liked_flag':False
        },
        {
            'text':'I really enjoyed the film and would recommend it to my friends',
            'liked_flag':True
        },
        {
            'text':'this movie is so fun that make me can\'t stop laughing',
            'liked_flag':True
        },
        {
            'text':'this movie is amazing, I love it so much.',
            'liked_flag':True
        },
        {
            'text':'this movie is terrible that make me fall aslep during the movie.',
            'liked_flag':False
        },
        {
            'text':'Soooooooo good!',
            'liked_flag':True
        },
        {
            'text':'What a good movie.',
            'liked_flag':True
        },
    ]

    for cat,cat_data in cats.items():
        c = add_cat(cat)
        for m in cat_data['movies']:
            add_movie(c,m['name'],m['director'],m['lead_actor'],m['description'],m['movie_image'],m['pub_date'])

    for user in users:
        add_user(user.get('username'),user.get('password'),user.get('is_superuser'),user.get('is_staff'))

    user1 = User.objects.get(username='Tom')
    user2 = User.objects.get(username='Root')
    user3 = User.objects.get(username='John')

    movie1 = Movie.objects.get(name='Roman Holiday') 
    movie2 = Movie.objects.get(name='The Matrix') 
    movie3 = Movie.objects.get(name='The Lord of the Rings: The Fellowship of the Ring') 
    movie4 = Movie.objects.get(name='Edge of Tomorrow') 
    movie5 = Movie.objects.get(name='The Silence of the Lambs') 
    movie6 = Movie.objects.get(name='The Truman Show') 
    movie7 = Movie.objects.get(name='Warai no daigaku') 
    movie8 = Movie.objects.get(name='The Shawshank Redemption') 
    movie9 = Movie.objects.get(name='Gone with the Wind') 
    movie10 = Movie.objects.get(name='Ant-Man') 

    add_comment(movie1,user1,comment[0].get('text'),comment[0].get('liked_flag'))
    add_comment(movie1,user2,comment[7].get('text'),comment[7].get('liked_flag'))
    add_comment(movie1,user3,comment[2].get('text'),comment[2].get('liked_flag'))
    add_comment(movie2,user1,comment[6].get('text'),comment[6].get('liked_flag'))
    add_comment(movie2,user3,comment[8].get('text'),comment[8].get('liked_flag'))
    add_comment(movie3,user2,comment[1].get('text'),comment[1].get('liked_flag'))
    add_comment(movie4,user1,comment[4].get('text'),comment[4].get('liked_flag'))
    add_comment(movie5,user2,comment[7].get('text'),comment[7].get('liked_flag'))
    add_comment(movie5,user1,comment[3].get('text'),comment[3].get('liked_flag'))
    add_comment(movie6,user3,comment[2].get('text'),comment[2].get('liked_flag'))
    add_comment(movie7,user2,comment[5].get('text'),comment[5].get('liked_flag'))
    add_comment(movie7,user3,comment[2].get('text'),comment[2].get('liked_flag'))
    add_comment(movie8,user1,comment[1].get('text'),comment[1].get('liked_flag'))
    add_comment(movie8,user2,comment[2].get('text'),comment[2].get('liked_flag'))
    add_comment(movie8,user3,comment[3].get('text'),comment[3].get('liked_flag'))
    add_comment(movie9,user2,comment[0].get('text'),comment[0].get('liked_flag'))
    add_comment(movie10,user1,comment[3].get('text'),comment[3].get('liked_flag'))
    


def add_cat(name):
    c= Category.objects.get_or_create(name=name)[0]
    c.save()
    return c

def add_movie(cat,name,director,lead_actor,description,image,pub_date):
    m = Movie.objects.get_or_create(category=cat,name=name,pub_date=pub_date)[0]
    m.director = director
    m.lead_actor = lead_actor
    m.description = description
    m.movie_image = image
    m.save()
    return m

def add_user(name,password,is_superuser,is_staff):
    u = User.objects.get_or_create(username=name)[0]
    u.set_password(password)
    u.is_superuser = is_superuser
    u.is_staff=is_staff
    u.save()
    return u

def add_comment(movie,user,text,liked_flag):
    c=Comment.objects.get_or_create(movie=movie,user=user)[0]
    c.text = text
    c.liked_flag = liked_flag
    c.save()
    return c


if __name__ == '__main__':
    populate()