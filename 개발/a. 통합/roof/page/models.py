from django.db import models

# Create your models here.
class Tag(models.Model):
    tag_id = models.AutoField('Tag ID', primary_key=True)
    title = models.CharField('TITLE' ,max_length=10)
    content = models.TextField('CONTENT')

class Category(models.Model):
    category_id = models.AutoField('Category ID', primary_key=True)
    title = models.CharField('TITLE' ,max_length=10)
    content = models.TextField('CONTENT')

class Member(models.Model):
    member_id = models.AutoField('Category ID', primary_key=True)
    name = models.CharField('TITLE' ,max_length=10)

class Post(models.Model):
    post_id = models.AutoField('Category ID', primary_key=True)
    title = models.CharField('TITLE' ,max_length=25)
    content = models.TextField('CONTENT', null=True, blank=True)
    photo_id = models.ForeignKey('Photo', on_delete=models.CASCADE) #
    '''
    photo_id1 = models.ForeignKey('Photo', on_delete=models.CASCADE)
    photo_id2 = models.ForeignKey('Photo', on_delete=models.CASCADE)
    photo_id3 = models.ForeignKey('Photo', on_delete=models.CASCADE)
    photo_id4 = models.ForeignKey('Photo', on_delete=models.CASCADE)
    photo_id5 = models.ForeignKey('Photo', on_delete=models.CASCADE)
    photo_id6 = models.ForeignKey('Photo', on_delete=models.CASCADE)
    photo_id7 = models.ForeignKey('Photo', on_delete=models.CASCADE)
    photo_id8 = models.ForeignKey('Photo', on_delete=models.CASCADE)
    photo_id9 = models.ForeignKey('Photo', on_delete=models.CASCADE)
    photo_id10 = models.ForeignKey('Photo', on_delete=models.CASCADE)
    '''
    date = models.DateTimeField('TIME', auto_now=True)
    category_title = models.ForeignKey('Category', on_delete=models.CASCADE)
    member_id = models.ForeignKey('Member', on_delete=models.CASCADE)
    tag_id = models.ForeignKey('Tag', on_delete=models.CASCADE) #
    '''
    tag_id1 = models.ForeignKey('Tag', on_delete=models.CASCADE)
    tag_id2 = models.ForeignKey('Tag', on_delete=models.CASCADE)
    tag_id3 = models.ForeignKey('Tag', on_delete=models.CASCADE)
    tag_id4 = models.ForeignKey('Tag', on_delete=models.CASCADE)
    tag_id5 = models.ForeignKey('Tag', on_delete=models.CASCADE)
    '''

class Photo(models.Model):
    photo_id = models.AutoField('Photo ID', primary_key=True)
    title = models.CharField('TITLE' ,max_length=25)
    source = models.CharField('Image Source' ,max_length=200)
    member_id = models.ForeignKey('Member', on_delete=models.CASCADE)
    post_id = models.ForeignKey('Post',on_delete=models.CASCADE)
    content = models.TextField('CONTENT', null=True, blank=True)
