from django.views.generic import DeleteView, UpdateView, ListView, DetailView, CreateView
from .models import Post
from django.urls import reverse, reverse_lazy

class BlogListView(ListView):
    model = Post
    template_name = "home.html"

class BlogDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"


    # def get_object(self):
    #     print(self.kwargs.get('pk'))
    #     return Post.objects.get(pk=self.kwargs.get('pk'))

class BlogCreateView(CreateView):
    model = Post
    template_name = "post_new.html"
    fields = ["title", "author", "body"]


class BlogUpdateView(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ["title", "body"]

class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy("home")

