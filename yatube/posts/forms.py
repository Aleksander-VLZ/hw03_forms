from django.forms import ModelForm

from .models import Post


class PostForm(ModelForm):
    class Meta:
        model = Post
        help_texts = {'group': 'Выберите группу', 'text': 'Введите сообщение'}
        fields = ["group", "text"]
