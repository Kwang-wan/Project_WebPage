from django.urls import re_path, path
from page import views



app_name = 'page'
urlpatterns = [

    #/page/member/yonghyun/
    re_path(r'^member/(?P<name>[-\w]+)/$', views.PageLV.as_view(), name='member_list'),

    #/page/member/yonghyun/game/
    re_path(r'^member/(?P<name>[-\w]+)/(?P<category>[-\w]+)/$', views.PageCaLV.as_view(), name='member_category_list'),
    
    #/page/member/yonghyun/game/game-title/
    re_path(r'^member/(?P<name>[-\w]+)/(?P<category>[-\w]+)/(?P<title>[-\w]+)/$', views.PageDV.as_view(), name='member_post_detail'),    

    #/page/member/yonghyun/game/game-title/game-photo-title/
    re_path(r'^member/(?P<name>[-\w]+)/(?P<category>[-\w]+)/(?P<title>[-\w]+)/(?P<photo_title>[-\w]+)$', views.PagePhotoDV.as_view(), name='member_photo_detail'),

    #/page/tag/supermario/
    re_path(r'^tag/(?P<tag>[-\w]+)/$', views.TagLV.as_view(), name='tag_list'),

    #/page/category/game/
    re_path(r'^category/(?P<category>[-\w]+)/$', views.CaLV.as_view(), name='category_list'),

    #/page/search/
    re_path(r'^search/$', views.SearchFormView.as_view(), name='search'),

]

