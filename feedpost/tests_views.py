from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Post, CustomUser, ParentProfile, GuestProfile,
Profile, Comment

# Create your tests here.


class TestViews(TestCase):
    def setUp(self):
        """
        set up a staff user and log them in
        to test the blog crud functionality
        """
        email = "test@test.com"
        password = "testpassword1234"
        username = "testFirst"
        is_parent = True
        user_model = get_user_model()
        self.user = user_model.objects.create_user(
            email=email, password=password, username=username, is_parent=True
        )
        log_in = self.client.login(
            email=email, password=password, is_parent=True, username=username
        )

        self.assertTrue(log_in)
        self.assertTrue(self.user.is_parent)

        # title = "test title"
        # slug = "testslug"
        # content = "testContent"
        # self.post = Post.objects.create(
        #     title=title, slug=slug, author=self.user, content=content
        # )
        # posts = Post.objects.all()

    def test_landing_page(self):

        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home.html")

    def test_welcome_page(self):

        response = self.client.get("/welcome_page")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "welcome_page.html")

    def test_parent_page(self):

        response = self.client.get("/parent")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "parent.html")

    def test_addchild_page(self):

        response = self.client.get("/add_child")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "add_child")

    def test_guest_page(self):

        response = self.client.get("/guest")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "guest.html")

    def test_get_edit_item_page(self):

        post = Post.objects.create(title='Testing1234')
        response = self.client.get(f'/post_detail/{post.slug}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'post_detail')

    # def test_post_page(self):
    #     '''
    #     test the blog page url
    #     '''
    #     response = self.client.get('/post_detail/')
    #     self.assertEqual(response.status_code, 200)
