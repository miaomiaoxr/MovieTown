from distutils.command.upload import upload
from lib2to3.pgen2.token import COMMENT
from tabnanny import verbose
from xml.parsers.expat import model
from django import views
from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

class Category(models.Model):
    NAME_MAX_LENGTH = 128

    name = models.CharField(max_length=NAME_MAX_LENGTH,unique=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)

    def save(self,*args,**kwargs):
        self.slug = slugify(self.name)
        super(Category,self).save(*args,**kwargs)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Movie(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    name = models.CharField(max_length=128,unique=True)
    director = models.CharField(max_length=128,blank=True)
    lead_actor = models.CharField(max_length=128,blank=True)
    movie_image = models.ImageField(upload_to='movie_image', blank=True)
    description = models.CharField(max_length=500,blank=True)
    pub_date = models.DateField(blank=True)
    upload_date = models.DateField(blank=True)
    slug = models.SlugField(unique=True)

    def save(self,*args,**kwargs):
        self.slug = slugify(self.name)
        super(Category,self).save(*args,**kwargs)

    

    def __str__(self) -> str:
        return self.name

class Comment(models.Model):
    COMMENT_MAX_LENGTH = 128

    user = models.ForeignKey(User,on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    text = models.CharField(max_length=COMMENT_MAX_LENGTH)
    liked_flag = models.BooleanField(default=False)

    def __str__(self) :
        return self.user.username +" "+str(self.movie)+" "+self.text+" "+ str(self.liked_flag)


class Page(models.Model):
    TITLE_MAX_LENGTH = 128
    URL_MAX_LENGTH = 200

    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    title = models.CharField(max_length=TITLE_MAX_LENGTH)
    url = models.URLField(max_length=URL_MAX_LENGTH)
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_image', blank=True)

    def __str__(self) :
        return self.user.username