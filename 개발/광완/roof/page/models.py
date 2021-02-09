from django.db import models
from django.urls import reverse

from page.fields import ThumbnailImageField

class Tag(models.Model):
    title = models.CharField('TITLE' ,max_length=10)
    slug = models.SlugField('SLUG', unique=True, allow_unicode=True, help_text='one word for title alias.')
    content = models.TextField('CONTENT', blank=True)
    
    def __str__(self):
        return self.title   

class Category(models.Model):
    title = models.CharField('TITLE' ,max_length=10)
    slug = models.SlugField('SLUG', unique=True, allow_unicode=True, help_text='one word for title alias.')
    content = models.TextField('CONTENT', blank=True)
    
    def __str__(self):
        return self.title    

class Member(models.Model):
    name = models.CharField('NAME' ,max_length=10)
    slug = models.SlugField('SLUG', unique=True, allow_unicode=True, help_text='one word for title alias.')    
    category_id = models.ManyToManyField('Category')
    
    def __str__(self):
        return self.name  

class Post(models.Model):
    title = models.CharField('TITLE' ,max_length=25)
    slug = models.SlugField('SLUG', unique=True, allow_unicode=True, help_text='one word for title alias.')
    content = models.TextField('CONTENT', blank=True)
    date = models.DateTimeField('TIME', auto_now_add=True)
    category_id = models.ForeignKey('Category', on_delete=models.CASCADE)
    member_id = models.ForeignKey('Member', on_delete=models.CASCADE)
    tag_id = models.ManyToManyField('Tag')

    class Meta:
        ordering = ('title',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('page:member_post_detail', args=(self.id,))


class Photo(models.Model):
    post_id = models.ForeignKey('Post', on_delete=models.CASCADE)
    title = models.CharField('TITLE' ,max_length=25)
    slug = models.SlugField('SLUG', unique=True, allow_unicode=True, help_text='one word for title alias.')
    image = ThumbnailImageField(upload_to='photo/%Y/%m')
    member_id = models.ForeignKey('Member', on_delete=models.CASCADE)
    content = models.TextField('CONTENT', blank=True)

    class Meta:
        ordering = ('title',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('page:member_photo_detail', args=(self.id,))