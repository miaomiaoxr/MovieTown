from django.shortcuts import render
from django.http import HttpResponse,Http404,JsonResponse
from django.shortcuts import redirect
from movie.models import Comment,Movie
from django.contrib.auth.decorators import login_required

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
    return render(request,'movie/index.html')

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
