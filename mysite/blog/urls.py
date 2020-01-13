from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
   path('', views.show_blogs, name='show_blogs'),
   path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.blog_detail, name='blog_detail'),
   path('<int:article_id>/share/', views.article_share, name='article_share'),
]
