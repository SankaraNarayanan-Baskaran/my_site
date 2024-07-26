from django.contrib import admin

# Register your models here.
from .models import Author,Post,Tag,Comment

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":("title",)}
    list_filter = ("tags","author","date",)
    list_display = ("title","author","date",)


class CommentAdmin(admin.ModelAdmin):
    list_display=("user_name","post")

admin.site.register(Author)
admin.site.register(Post,PostAdmin)
admin.site.register(Tag)
admin.site.register(Comment,CommentAdmin)