from xml.etree.ElementTree import Comment
from django.shortcuts import render
from django.http import HttpResponse,Http404
from django.shortcuts import redirect
from movie.models import Comment
from django.contrib.auth.decorators import login_required

# Create your views here.
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
        try:
            c = Comment.objects.get(user=request.user,movie=request.movie)
        except Comment.DoesNotExist:
            raise Http404("No Comment matches the given query.")
        c.delete()
        return HttpResponse('ok')



def index(request):
    return render(request,'movie/index.html')