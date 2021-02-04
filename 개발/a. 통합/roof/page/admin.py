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
    list_display = ('post_id', 'title', 'content', 'photo_list','date','category_title','member_id','tag_list')
    def photo_list(self, obj):
        return ', '.join(o for o in obj.title.all())
    def tag_list(self, obj):
        return ', '.join(o for o in obj.title.all())    


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('photo_id', 'title', 'source', 'member_id', 'post_id', 'content')