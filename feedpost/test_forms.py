# from django.test import TestCase
# from .forms import PostForm, RegisterForm, ParentForm, GuestForm, CommentForm, ChildForm



# class TestRegisterForm(TestCase):
#     def test_register_name_is_required(self):
#         form = RegisterForm({"username": ""})
#         self.assertFalse(form.is_valid())
#         self.assertIn("username", form.errors.keys())
#         self.assertEqual(form.errors["username"][0], "This field is required.")

#     def test_fields_are_explicit_in_form_metaclass(self):
#         form = RegisterForm()
#         self.assertEqual(
#             form.Meta.fields, ["is_guest", "is_parent", "username", "email"]
#         )


# class TestPostForm(TestCase):
#     def test_postform_title_is_required(self):
#         form = PostForm({"title": ""})
#         self.assertFalse(form.is_valid())
#         self.assertIn("title", form.errors.keys())
#         self.assertEqual(form.errors["title"][0], "This field is required.")

#     def test_postform_is_valid(self):
#         form = PostForm(
#             data={
#                 "title": "Testing", "slug": "testing",
#                 "content": "This is a test"
#             }
#         )

#         self.assertTrue(form.is_valid())


# class TestParentForm(TestCase):
#     def test_postform_title_is_required(self):
#         form = ParentForm({"parent_name": ""})
#         self.assertFalse(form.is_valid())
#         self.assertIn("parent_name", form.errors.keys())
#         self.assertEqual(
#             form.errors["parent_name"][0], "This field is required.")

#     def test_profile_image_field_is_not_required(self):
#         form = ParentForm({"parent_name": "Daniel Porras"})
#         self.assertTrue(form.is_valid())


# class TestCommentForm(TestCase):
#     def test_register_name_is_required(self):
#         form = CommentForm({"post": ""})
#         self.assertFalse(form.is_valid())
#         self.assertIn("post", form.errors.keys())
#         self.assertEqual(form.errors["post"][0], "This field is required.")

#     def test_fields_are_explicit_in_form_metaclass(self):
#         form = CommentForm()
#         self.assertEqual(form.Meta.fields, "__all__")


# class TestChildForm(TestCase):
#     def test_postform_title_is_required(self):
#         form = ChildForm({"child_name": ""})
#         self.assertFalse(form.is_valid())
#         self.assertIn("child_name", form.errors.keys())
#         self.assertEqual(
#             form.errors["child_name"][0], "This field is required.")

#     def test_profile_image_field_is_not_required(self):
#         form = ChildForm(
#             {"child_name": "Theo Porras", "birthdate": "03/11/2021"})

#         self.assertTrue(form.is_valid())


# class TestGuestForm(TestCase):
#     def test_guest_guest_name_is_required(self):
#         form = GuestForm({"guest_name": ""})
#         self.assertFalse(form.is_valid())
#         self.assertIn("guest_name", form.errors.keys())
#         self.assertEqual(
#             form.errors["guest_name"][0], "This field is required.")

#     def test_guest_image_field_is_not_required(self):
#         form = GuestForm(
#             {
#                 "guest_name": "Alonso Porras",
#             }
#         )

#         self.assertFalse(form.is_valid())
