# URL 설계

| URL 패턴                                         | 뷰 이름                      | 템플릿 파일명             |
| ------------------------------------------------ | ---------------------------- | ------------------------- |
| /                                                | HomeView(TemplateView)       | home.html                 |
| /page/                                           | ~~//PageTV(TemplateView)//~~ |                           |
| /page/yonghyun/                                  | PageLV(ListView)             | member_list.html          |
| /page/yonghyun/game/                             | PageCaLV(ListView)           | member_category_list.html |
| /page/yonghyun/game/game-title/                  | PageDV(DetailView)           | member_post_detai.html    |
| /page/yonghyun/game/game-title/game-photo-title/ | PagePhotoDV(DetailView)      | member_photo_detail.html  |
| /tag/                                            | ~~//TagTV(TemplateView)//~~  |                           |
| /tag/supermario/                                 | TagLV(ListView)              | tag_list.html             |
| /category/                                       | ~~//CaTV(TemplateView)//~~   |                           |
| /category/game/                                  | CaLV(ListView)               | category_list.html        |



ListView

DetailView

TemplateView

<app_label>/<model_name 소문자>_<template_name_suffix>.html

| Generic View 이름 | template_name_suffix | 예시(page 앱의 post 모델인 경우) |
| ----------------- | -------------------- | -------------------------------- |
| ListView          | _list                | page/post_list.html              |
| DetailView        | _detail              | page/post_detail.html            |

TemplateView, RedirectView 등은 모델을 지정할 필요가 없는 제네릭 뷰이므로, 디폴트 템플릿명을 갖지 않습니다.







ArchiveIndexView

YearArchiveView

MonthArchiveView

DayArchiveView

TodayArchiveView





view.py

```python
from django.views.generic import ListView

class PostLV(ListView):
```



post_all.html

```python
{% extend "base.html" %}


```

