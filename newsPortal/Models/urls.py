from django.urls import path
from.views import PostListView, PostDetail, PostListViewSearch, CreateNews, NewsUpdate, NewsDelete,ArticleUpdate,CreateArticle, ArticleDelete


urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('<int:pk>', PostDetail.as_view(), name='post_detail'),
    path('search/', PostListViewSearch.as_view()),
    path('news/create', CreateNews.as_view()),
    path('news/<int:pk>/edit', NewsUpdate.as_view(), name='update_news'),
    path('news/<int:pk>/delete', NewsDelete.as_view()),
    path('article/create', CreateArticle.as_view()),
    path('article/<int:pk>/edit', ArticleUpdate.as_view(), name='update_article'),
    path('article/<int:pk>/delete', ArticleDelete.as_view())
]