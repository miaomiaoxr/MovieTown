from django.shortcuts import render
from django.http import HttpResponse,Http404,JsonResponse
from django.shortcuts import redirect
from movie.models import Comment
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