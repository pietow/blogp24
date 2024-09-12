from django.views.generic import DeleteView, UpdateView, ListView, DetailView, CreateView
from .models import Post
from django.urls import reverse, reverse_lazy
from django.views import View
from django.shortcuts import redirect

class BlogListView(ListView):
    model = Post
    template_name = "home.html"

    def get(self, request, *args, **kwargs):
        print('View is called')
        return super().get(request, *args, **kwargs)

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

class ThemeView(View):
    def get(self, request):
        theme = request.session.get('theme', 'light')
        if theme == 'light':
            request.session['theme'] = 'dark'
        else:
            request.session['theme'] = 'light'
        print(request.session.get('theme'))
        print(request.session['theme'])
        return redirect(request.META.get('HTTP_REFERER'))
        
        



