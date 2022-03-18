from django.shortcuts import render
from django.http import HttpResponse,Http404,JsonResponse
from django.shortcuts import redirect
from movie.models import Comment,Movie
from django.contrib.auth.decorators import login_required
from movie.models import Category
from movie.models import Movie
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage, InvalidPage

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


def moviepage(request,movie_name_slug):
    # Create a context dictionary which we can pass
    # to the template rendering engine.
    context_dict = {}
    try:
        # Can we find a category name slug with the given name?
        # If we can't, the .get() method raises a DoesNotExist exception.
        # The .get() method returns one model instance or raises an exception.
        category = Movie.objects.get(slug=movie_name_slug)
        comments= Comment.objects.filter(movie=category)
        like_count=Comment.objects.filter(movie=category,liked_flag=True).count()
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