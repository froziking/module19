import django_filters
from django_filters import FilterSet, DateFilter
from django.forms import DateInput  # Импортируем DateInput из django.forms
from .models import Post


class PostFilter(FilterSet):
    # Фильтр по имени автора
    author = django_filters.CharFilter(
        field_name='author__username',
        lookup_expr='icontains',
        label='Автор (поиск по имени)'
    )

    # Фильтр по заголовку
    heading = django_filters.CharFilter(
        field_name='heading',
        lookup_expr='icontains',
        label='Заголовок'
    )

    # Фильтр по дате (позже чем)
    datatime_in_after = DateFilter(
        field_name='datatime_in',
        lookup_expr='gt',
        label='Дата публикации (позже чем)',
        widget=DateInput(attrs={'type': 'date'})  # Используем DateInput из django.forms
    )

    class Meta:
        model = Post
        fields = []  # Оставляем пустым, так как фильтры определены вручную


