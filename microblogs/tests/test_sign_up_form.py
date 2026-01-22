from django.test import TestCase

from microblogs.forms import SignUpForm

from django import forms


class SignUpFormTestCase(TestCase):
    def setUp(self):
        self.form_input = {
            'first_name': 'John',
            'last_name': 'Doe',
            'username': '@johndoe',
            'email': 'johndoe@example.org',
            'bio':'my bio',
            'new_password':'Password123',
            'password_confirmation':'Password123',
        }
    def test_valid_sign_up_form(self):
        form = SignUpForm(data=self.form_input)
        self.assertTrue(form.is_valid())

    def test_form_has_necessary_fields(self):
        form = SignUpForm()
        self.assertIn('first_name', form.fields)
        self.assertIn('last_name', form.fields)
        self.assertIn('username', form.fields)
        username_field = form.fields['username']
        username_field_widget = form.fields['username'].widget
        self.assertTrue(isinstance(username_field, forms.CharField))
        self.assertTrue(isinstance(username_field_widget, forms.TextInput))
        self.assertIn('email', form.fields)
        email_field = form.fields['email']
        self.assertTrue(isinstance(email_field, forms.EmailField))
        self.assertIn('bio', form.fields)
        self.assertIn('new_password', form.fields)
        new_password_widget = form.fields['new_password'].widget
        self.assertTrue(isinstance(new_password_widget, forms.PasswordInput))
        self.assertIn('password_confirmation', form.fields)
        password_confirmation_widget = form.fields['password_confirmation'].widget
        self.assertTrue(isinstance(password_confirmation_widget, forms.PasswordInput))

    def test_form_uses_model_validation(self):
        self.form_input['username'] = 'badusername'
        form = SignUpForm(data=self.form_input)
        self.assertFalse(form.is_valid())

    def test_password_must_contain_uppercase_character(self):
        self.form_input['new_password'] = 'password123'
        self.form_input['password_confirmation'] = 'password123'
        form = SignUpForm(data=self.form_input)
        self.assertFalse(form.is_valid())

    def test_password_must_contain_lowercase_character(self):
        self.form_input['new_password'] = 'PASSWORD123'
        self.form_input['password_confirmation'] = 'PASSWORD123'
        form = SignUpForm(data=self.form_input)
        self.assertFalse(form.is_valid())

    def test_password_must_contain_number(self):
        self.form_input['new_password'] = 'Password'
        self.form_input['password_confirmation'] = 'Password'
        form = SignUpForm(data=self.form_input)
        self.assertFalse(form.is_valid())
    def test_new_password_and_password_confirmation_must_match(self):
        self.form_input['password_confirmation'] = 'WrongPassword123'
        form = SignUpForm(data=self.form_input)
        self.assertFalse(form.is_valid())
