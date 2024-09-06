import os
import django
from blog.models import Post
from django.db.models import Value
from django.contrib.auth.models import User

# Set the Django settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_project.settings")

# Setup Django
django.setup()

# from django.db import connection
# # Clear queries before testing
# connection.queries = []

# Post.objects.values('id')
# print(connection.queries)  # This will show the single query fetching only 'id'

# Post.objects.only('id')
# print(connection.queries)  # This shows the initial query fetching only 'id'

# posts_only = Post.objects.only('id')
# for post in posts_only:
#     print(post.title)  # This triggers additional queries for the 'title' field
# print(connection.queries)  # T



