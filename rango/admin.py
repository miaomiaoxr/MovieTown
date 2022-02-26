from django.contrib import admin
from rango.models import Category,Page,Comment,Movie
from rango.models import UserProfile

class PageAdmin(admin.ModelAdmin):
    list_display = ('title','category','url')

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

class CommentAdmin(admin.ModelAdmin):
    list_display = ('user','movie', 'text','liked_flag')

# class MovieAdmin(admin.ModelAdmin):
#     list_display = ('title',)

admin.site.register(Category,CategoryAdmin)
admin.site.register(Page,PageAdmin)
admin.site.register(UserProfile)
admin.site.register(Comment,CommentAdmin)
# admin.site.register(Movie,MovieAdmin)
