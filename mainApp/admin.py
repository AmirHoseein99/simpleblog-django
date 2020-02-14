from django.contrib import admin
from .models import Post, Comment
# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):

    list_display = ('title', 'slug', 'author', 'date_of_creation')
    list_filter = ('date_of_creation', 'author')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'date_of_creation'
    ordering = ('date_of_creation',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'post', 'created', 'active')
    list_filter = ('active', 'created', )
    search_fields = ('name', 'email', 'body')
