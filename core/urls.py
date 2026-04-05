from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('hello/', views.hello_world, name='hello_world'),
    
    path('greet/<str:name>/', views.greet_user, name='greet_user'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    path('blog/<slug:slug>/', views.blog_post, name='blog_post'),

    path('test/', views.test_routing, name='test_routing'),
]
