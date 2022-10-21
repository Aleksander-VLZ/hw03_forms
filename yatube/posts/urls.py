from django.urls import path

from posts import views

app_name = 'posts'

urlpatterns = [
    #  Главная страница
    path('', views.index, name='index'),
    #  Страница сообществ, slug перед переменной - слова и цифры
    path('group/<slug:slug>/', views.group_posts, name='group_list'),
    # Профайл пользователя
    path('profile/<str:username>/', views.profile, name='profile'),
    # Просмотр записи
    path('posts/<int:post_id>/', views.post_detail, name='post_detail'),
    # Создание нового поста
    path('create/', views.post_create, name='post_create'),
    # Редактирование поста
    path('posts/<int:post_id>/edit/', views.post_edit, name='post_edit'),
]
