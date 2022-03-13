from django import template
from movie.models import Comment,User

register = template.Library()

# @register.inclusion_tag('registration/user_profile.html')

# def get_category_list(current_category=None):
#     return {'categories': Category.objects.all(),
#             'current_category':current_category}

# def get_comment_list(current_user=None):
#     return {'comments':Comment.objects.all(),
#             'current_user':current_user}