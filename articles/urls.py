from django.urls import path, include
from .views import ArticleListView, ArticleDetailView, CreatePostView, ArticleUpdate, ArticleDelete
from django.urls import path 
from .import views

urlpatterns = [
    path('', ArticleListView.as_view(), name='home'),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='detail'),
    path('create/', CreatePostView.as_view(), name='create'),
    path('create/<int:pk>/', ArticleUpdate.as_view(), name='article_edit'),
    path('delete/<int:pk>/', ArticleDelete.as_view(), name='delete'),  
]

