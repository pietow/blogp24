from django.urls import path
from .views import ThemeView, BlogDeleteView, BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView

urlpatterns = [
    path("", BlogListView.as_view(), name='home'),
    path("theme/", ThemeView.as_view(), name='toggle_theme'),
    path("post/<int:pk>/", BlogDetailView.as_view(), name='post_detail'),
    path("post/new/", BlogCreateView.as_view(), name='post_new'), 
    path("post/<int:pk>/edit/", BlogUpdateView.as_view(), name='post_edit'), 
    path("post/<int:pk>/delete/", BlogDeleteView.as_view(), name='post_delete'), #new

]
