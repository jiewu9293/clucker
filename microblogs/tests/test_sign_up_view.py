from django.test import TestCase

from microblogs.forms import SignUpForm
from django.urls import reverse

class SignUpViewTestCase(TestCase):
    def setUp(self):
        self.url = reverse('sign_up')
        self.form_input = {
            'first_name': 'John',
            'last_name': 'Doe',
            'username': '@johndoe',
            'email': 'johndoe@example.org',
            'bio': 'my bio',
            'new_password': 'Password123',
            'password_confirmation': 'Password123',
        }
    def test_sign_up_url(self):
        self.assertEqual(self.url,'/sign_up/')
    def test_get_sign_up(self):
        url = reverse('sign_up')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,'sign_up.html')
        form = response.context['form']
        self.assertTrue(isinstance(form,SignUpForm))
        self.assertFalse(form.is_bound)
    def test_unsuccessful_sign_up(self):
        url = reverse('sign_up')
        self.form_input['username']='BAD_USERNAME'
        response = self.client.post(self.url,self.form_input)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,'sign_up.html')
        form = response.context['form']
        self.assertTrue(isinstance(form,SignUpForm))
        self.assertTrue(form.is_bound)
    def test_successful_sign_up(self):
        response = self.client.post(self.url, self.form_input,follow=True)
        response_url = reverse('feed')
        self.assertRedirects(response,response_url,status_code=302,target_status_code=200)
        self.assertTemplateUsed(response, 'feed.html')
