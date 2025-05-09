from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm
from .filters import PostFilter
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin


# Create your views here.

class PostListView(ListView):
    model = Post
    ordering = 'heading'
    template_name = 'Posts.html'
    context_object_name = 'posts'
    paginate_by = 10


class PostDetail(DetailView):
    model = Post
    template_name = 'Post.html'
    context_object_name = 'post'


class PostListViewSearch(ListView):
    model = Post
    ordering = 'heading'
    template_name = 'search.html'
    context_object_name = 'posts_search'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Добавляем в контекст объект фильтрации.
        context['filterset'] = self.filterset
        return context


# class NewsListView(ListView):
#     model = Post
#     ordering = 'heading'
#     template_name = 'create_news.html'
#     context_object_name = 'news'
#
#     def get_queryset(self):
#         return Post.objects.filter(choice=Post.news)


class CreateNews(CreateView, PermissionRequiredMixin):
    permission_required = ('Models.add_post', )
    form_class = PostForm
    model = Post
    template_name = 'create_news.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.choice = 'NE'
        return super().form_valid(form)


class NewsUpdate(UpdateView, LoginRequiredMixin, PermissionRequiredMixin):
    permission_required = ('Models.change_post', )
    form_class = PostForm
    model = Post
    template_name = 'create_news.html'
    login_url = '/accounts/login/'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.choice = 'NE'
        return super().form_valid(form)


class NewsDelete(DeleteView, PermissionRequiredMixin):
    permission_required = ('Models.delete_post', )
    model = Post
    template_name = 'delete_news.html'
    success_url = reverse_lazy('post_list')


class CreateArticle(CreateView, PermissionRequiredMixin):
    permission_required = ('Models.add_post',)
    form_class = PostForm
    model = Post
    template_name = 'article_edit.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.choice = 'AR'
        return super().form_valid(form)


class ArticleUpdate(UpdateView, LoginRequiredMixin, PermissionRequiredMixin):
    permission_required = ('Models.change_post',)
    form_class = PostForm
    model = Post
    template_name = 'article_edit.html'
    login_url = '/accounts/login/'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.choice = 'AR'
        return super().form_valid(form)


class ArticleDelete(DeleteView, PermissionRequiredMixin):
    permission_required = ('Models.delete_post',)
    model = Post
    template_name = 'article_delete.html'
    success_url = reverse_lazy('post_list')
