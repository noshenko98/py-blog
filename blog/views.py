from django.core.paginator import Paginator
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView

from blog.models import Post, Commentary


def index(request):
    posts = Post.objects.all().order_by('-created_time')
    paginator = Paginator(posts, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {"posts": page_obj,
               }
    return render(request, "blog/index.html", context=context)

class PostDetailView(DetailView):
    model = Post


class CommentCreateView(CreateView):
    model = Commentary
    fields = ['content']
    template_name = "blog/post_detail.html"
    success_url = reverse_lazy("post_detail")

