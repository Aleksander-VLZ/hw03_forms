from django.core.paginator import Paginator

LAST_POSTS: int = 10


def paginate_posts(queryset, request, LAST_POSTS: int):
    paginator = Paginator(queryset, LAST_POSTS)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return {
        'page_obj': page_obj,
    }
