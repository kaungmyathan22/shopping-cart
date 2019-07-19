from django.test import TestCase, Client
from django.urls import reverse, resolve
from model_mommy import mommy


# class TestMovieListPage(TestCase):

#     def setUp(self):

#         self.client = Client()

#         self.url = reverse("core:list")

#         self.response = self.client.get(self.url)

#     def test_page_status(self):

#         self.assertEqual(self.response.status_code, 200)

#     def test_template_used(self):

#         self.assertTemplateUsed(self.response, 'core/movie_list.html')

#     def test_view_fun(self):

#         view_fun = resolve(self.url)

#         self.assertEqual(view_fun.func.view_class, views.MovieListView)
