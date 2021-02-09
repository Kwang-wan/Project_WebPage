from django.contrib import admin
from page.models import Tag, Category, Member, Post, Photo

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ( 'title', 'content')
    prepopulated_fields = {'slug': ('title',)}    

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ( 'category_title', 'content')
    prepopulated_fields = {'slug': ('category_title',)}    

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ( 'name', 'category_list')
    prepopulated_fields = {'slug': ('name',)}
    def category_list(self, obj):
        return ', '.join(o.title for o in obj.category_id.all())    

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ( 'title', 'content', 'date','category_id','member_id','tag_list') 
    prepopulated_fields = {'slug': ('title',)}
    '''def photo_list(self, obj):
        return ', '.join(o.title for o in obj.photo_id.all())'''
    def tag_list(self, obj):
        return ', '.join(o.title for o in obj.tag_id.all())    


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('title', 'source', 'member_id', 'post_id', 'content')  
    prepopulated_fields = {'slug': ('title',)}