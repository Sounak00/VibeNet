from django.urls import path
from . import views

urlpatterns = [

    path('', views.home),
    path('signup/', views.signup, name='signup'),
    path('loginn/', views.loginn, name='loginn'),
    path('logoutt/', views.logoutt, name='logoutt'),
    path('upload/', views.upload, name='upload'),
    path('like-post/<str:id>', views.likes, name='like-post'),
    path('#<str:id>', views.home_posts, name='home_post'),
    path('explore/', views.explore, name='explore'),
    path('profile/<str:id_user>', views.profile),
    path('follow', views.follow, name='follow'),
    path('delete/<str:id>', views.delete),
    path('search-results/', views.search_results, name='search_results'),
]