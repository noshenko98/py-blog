from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, ListView

from blog.models import Post, Commentary


# def index(request):
#     post_list = Post.objects.all().order_by('-created_time')
#     paginator = Paginator(post_list, 5)
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#     context_object_name = "post_list"
#     context = {"posts": page_obj,
#                }
#     return render(request, "blog/index.html", context=context)

class PostList(LoginRequiredMixin, ListView):
    model = Post
    paginate_by = 5
    context_object_name = "post_list"


class PostDetailView(DetailView):
    model = Post


class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Commentary
    fields = ["content"]
    template_name = "blog/post_detail.html"
    success_url = reverse_lazy("blog:post-detail", kwargs={"pk" : 1})
