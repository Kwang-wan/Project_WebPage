from django.contrib import admin
from page.models import Tag, Category, Member, Post, Photo

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('tag_id', 'title', 'content')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_id', 'title', 'content')

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('member_id', 'name')

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('post_id', 'title', 'content', 'photo_id','date','category_title','member_id','tag_id')
    '''
    list_display = ('post_id', 'title', 'content', 'photo_id1', 'photo_id2', 'photo_id3','photo_id4','photo_id5','photo_id6','photo_id7','photo_id8','photo_id9','photo_id10','date','category_title','member_id','tag_id1','tag_id2','tag_id3','tag_id4','tag_id5')
    '''

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('photo_id', 'title', 'source', 'member_id', 'post_id', 'content')