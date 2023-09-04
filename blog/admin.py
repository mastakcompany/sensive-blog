from django.contrib import admin
from blog.models import Post, Tag, Comment


@admin.display(description='DisplayComment')
def display_comment(obj):
    return f'{obj.author.username} under {obj.post.title}'


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    raw_id_fields = ('likes', 'tags')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    raw_id_fields = ('post', 'author')
    list_display = (display_comment,)


admin.site.register(Tag)
