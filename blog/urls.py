from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('create_post/',views.create_post,name='create_post'),
    path('post_list/',views.post_list,name='post_list'),
    path('post_detail/<int:year>/<int:month>/<int:day>/<int:id>/',views.post_detail,name='post_detail'),
    path('post_edit/<int:id>/',views.post_edit,name='post_edit'),
    path('post_delete/<int:id>/',views.post_delete,name='post_delete'),
    path('draft_list/',views.draft_list,name='draft_list'),
    path('search/',views.post_search,name='post_search'),
    path('<slug:tag_slug>/',views.post_list,name='post_list_by_tag'),
    
    
]