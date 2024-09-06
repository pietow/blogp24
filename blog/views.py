from django.views.generic import ListView, DetailView
from .models import Post
from django.urls import reverse

class BlogListView(ListView):
    model = Post
    template_name = "home.html"

class BlogDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"

    # def get_context_data(self, **kwargs):
    #     print(self.kwargs)
    #     print(Post.objects.get(pk=self.kwargs['pk']))
    #     return super().get_context_data(**kwargs)