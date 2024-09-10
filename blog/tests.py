from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from .models import Post


class BlogTests(TestCase):

    @classmethod
    def setUpTestData(cls):

        cls.user = get_user_model().objects.create_user(
            username="testuser", email="test@gmail.com",
            password="secret"
        )

        cls.post = Post.objects.create(
            title='A good title',
            body="Nice body content",
            author=cls.user
        )

    def test_post_deleteview(self):
        response = self.client.post(reverse('post_delete', kwargs={"pk": 1}))
        self.assertEqual(Post.objects.last(), None) # confirm that no post entries are stored/ or deleted
        self.assertEqual(response.status_code, 302)

    def test_post_model(self):
        self.assertEqual(self.post.title, 'A good title')    
        self.assertEqual(self.post.body, 'Nice body content')    
        self.assertEqual(self.post.author.username, 'testuser')    
        self.assertEqual(str(self.post), 'A good title')    
        self.assertEqual(self.post.get_absolute_url(), '/post/1/')    

    def test_url_exists_at_correct_location_listview(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_url_exists_at_correct_location_detailview(self):
        response = self.client.get('/post/1/')
        self.assertEqual(response.status_code, 200)

    def test_post_listview(self):
        response = self.client.get(reverse('home'))
        self.assertContains(response, 'Nice body content')
        self.assertTemplateUsed(response, "home.html")

    def test_post_listview(self):
        response = self.client.get(reverse('post_detail',
                                kwargs={'pk': self.post.pk}))
        no_response = self.client.get('/post/1000/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)

    def test_post_createview(self):
        response = self.client.post(
            reverse('post_new'),
            {
                "title": "new title",
                "body": "New text",
                "author": self.user.id,
            }
        )

        self.assertEqual(response.status_code, 302)
        self.assertEqual(Post.objects.last().title, "new title")
        self.assertEqual(Post.objects.last().body, "New text")

    def test_post_updateview(self):
        response = self.client.post(
            #reverse("post_edit", args="1"),
            reverse('post_edit', kwargs={"pk": 1}),
            {
                "title": "Updated title",
                "body": "Updated text",
            }
        )

        self.assertEqual(response.status_code, 302)
        self.assertEqual(Post.objects.last().title, "Updated title")
        self.assertEqual(Post.objects.last().body, "Updated text")


        

    