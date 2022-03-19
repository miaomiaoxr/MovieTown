#from email import message
from turtle import update
from django.shortcuts import render
from django.http import HttpResponse,Http404,JsonResponse,HttpResponseRedirect
from django.shortcuts import redirect
from movie.models import Comment,Movie
from django.contrib.auth.decorators import login_required
from movie.models import Category
from movie.models import Movie
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage, InvalidPage
from movie.bing_search import run_query
from django.db.models import Q
from django.contrib import messages

# Create your views here.
@login_required
def delete_comments_user_profile(request,pk):
    if request.is_ajax():
        comment = Comment.objects.get(pk=pk)
        comment.delete()
        return JsonResponse({"message":"success"})
    
    return JsonResponse({"message":"Wrong Route"})

@login_required
def user_profile(request):

    if request.method == 'GET':
        context_dict = {}

        try:
            comments = Comment.objects.filter(user=request.user)

            context_dict['comments'] = comments
        except:
            context_dict['comments'] = None
        return render(request,'registration/user_profile.html',context=context_dict) 
    
    if request.method == 'DELETE':
        
        return HttpResponse('ok')



def index(request):
    # yxh test, can be deleted
    category_list = Category.objects.all()
    context_dict = {'categories': category_list}
    return render(request,'movie/index.html', context = context_dict)
    # return render(request,'movie/index.html')
    
    
    
def show_category(request, category_name_slug):
    # Create a contextual dictionary to be passed to the template rendering engine later
    context_dict = {}
    
    try:
        category_list = Category.objects.all()
        
        # Find the corresponding category by passing in the category alias
        category = Category.objects.get(slug = category_name_slug)
    
        # Find all movies with this category by foreign key
        movies = Movie.objects.filter(category=category)
        
        # Display 1 item per page as specified, split
        paginator = Paginator(movies, 12) 
        
        
        page = request.GET.get('page', default = '1')
        
        try:
            movies = paginator.page(page)
        except PageNotAnInteger:
            # If the number of pages requested is not an integer, the first page is returned.
            books = paginator.page(1)
        except InvalidPage:
            # If the requested page does not exist, redirect the page
            return HttpResponse('The content of the page cannot be found')
        except EmptyPage:
            # If the requested page is not within the legal page count, the last page of the result is returned.
            books = paginator.page(paginator.num_pages)
            
        context_dict['categories'] = category_list
        context_dict['category'] = category
        context_dict['movies'] = movies
        
    except Category.DoesNotExist:
        context_dict['categories'] = None
        context_dict['category'] = None
        context_dict['movies'] = None
        
        
    return render(request, 'movie/category.html', context = context_dict)

most_like_list = None

def moviepage(request,movie_name_slug):
    # Create a context dictionary which we can pass
    # to the template rendering engine.
    context_dict = {}
    context_dict['flag1']=False
    category_list = Category.objects.all()
    context_dict['categories'] = category_list
    try:
        # Can we find a category name slug with the given name?
        # If we can't, the .get() method raises a DoesNotExist exception.
        # The .get() method returns one model instance or raises an exception.
        category = Movie.objects.get(slug=movie_name_slug)
        comments= Comment.objects.filter(movie=category)
        like_count=Comment.objects.filter(movie=category,liked_flag=True).count()
        if request.user.is_authenticated:
            result= Comment.objects.filter(movie=category,user=request.user)[0]
            context_dict['flag1']=result.liked_flag
        # Retrieve all of the associated pages.
        # The filter() will return a list of page objects or an empty list.
        # Adds our results list to the template context under name pages.
        # We also add the category object from
        # the database to the context dictionary.
        # We'll use this in the template to verify that the category exists.
        context_dict['movie'] = category
        context_dict['comments'] =comments
        context_dict['count'] = like_count
    except Movie.DoesNotExist:
        # We get here if we didn't find the specified category.
        # Don't do anything -
        # the template will display the "no category" message for us.
        context_dict['movie'] = None
        # Go render the response and return it to the client.

    return render(request, 'movie/movie.html', context=context_dict)


def homepage(request):
    context_dict = {}
    movies = None
    try:
        movies_top3 = Movie.objects.all()[:3]
        movies_4_10 = Movie.objects.all()[4:10]
        movies_update = Movie.objects.order_by('pub_date')[:5]
        context_dict['movies_top3'] = movies_top3
        context_dict['movies_4to10'] = movies_4_10
        context_dict['movies_update'] = movies_update

    except Movie.DoesNotExist:
        context_dict['movies'] = None
        context_dict['movies_4to10'] = None
        context_dict['movies_update'] = None
        
    return render(request, 'movie/homepage.html', context = context_dict)


def search(request):
    context_dict = {}
    movies = None
    try:
        if request.GET['search_txt']!="":
            query=request.GET['search_txt']
            movies = Movie.objects.filter(Q(name__icontains=query) | Q(director__icontains=query) | Q(lead_actor__icontains=query) | Q(description__icontains=query) | Q(pub_date__icontains=query))
        
        paginator = Paginator(movies, 12) 
        page = request.GET.get('page', default = '1')
        
        try:
            movies = paginator.page(page)
        except PageNotAnInteger:
            # If the number of pages requested is not an integer, the first page is returned.
            movies = paginator.page(1)
        except InvalidPage:
            # If the requested page does not exist, redirect the page
            return HttpResponse('The content of the page cannot be found')
        except EmptyPage:
            movies = paginator.page(paginator.num_pages)
        context_dict['movies'] = movies
    except Category.DoesNotExist:
        context_dict['movies'] = None
    return render(request, 'movie/search_css.html', context = context_dict)


@login_required
def submit_func(request,movie_name_slug):
    user=request.user
    movie = Movie.objects.get(slug=movie_name_slug)
    comments= Comment.objects.filter(movie=movie,user=user)
    if comments:
        if request.GET['comment_txt']!="":
            comment=Comment.objects.get(movie=movie,user=user)
            comment.text=request.GET['comment_txt']
            comment.save()
        else:
            messages.info(request,"Comment cannot be empty")
    else:
        if request.GET['comment_txt']!="":
            comment=Comment.objects.create(movie=movie,user=user)
            comment.text=request.GET['comment_txt']
            comment.save()
        else:
            messages.info(request,"Comment cannot be empty")
    return moviepage(request,movie_name_slug)


@login_required
def like_func(request,movie_name_slug):
    user=request.user
    movie = Movie.objects.get(slug=movie_name_slug)
    comment,created= Comment.objects.get_or_create(movie=movie,user=user)
    if created:
        comment.liked_flag=True
        comment.save()
    else:
        comment.liked_flag=not comment.liked_flag
        comment.save()
    return moviepage(request,movie_name_slug)

