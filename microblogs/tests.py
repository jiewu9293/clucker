from django.test import TestCase
from django.core.exceptions import ValidationError
from .models import User
class UserModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            '@johndoe',
            first_name='John',
            last_name='Doe',
            email='john@example.com',
            password='password123',
            bio='this is a bio'
        )
    def test_valid_user(self):
        self.assert_user_is_valid()

    def test_username_can_be_30_characters_long(self):
        self.user.username = '@'+'x'*29
        self.assert_user_is_valid()

    def test_username_can_not_be_over_30_characters_long(self):
        self.user.username = '@' + 'x' * 30
        self.assert_user_is_invalid()

    def test_username_must_start_with_at_symbol(self):
        self.user.username = 'johndoe'
        self.assert_user_is_invalid()
    def test_username_must_contain_only_alphanumericals_after_at(self):
        self.user.username = '@john!oe'
        self.assert_user_is_invalid()
    def test_username_must_contain_at_least_3_alphanumericals_after_at(self):
        self.user.username = '@jo'
        self.assert_user_is_invalid()
    def test_username_may_contain_numbers(self):
        self.user.username = '@johndoe2'
        self.assert_user_is_valid()
    def test_username_must_contain_only_one_at(self):
        self.user.username = '@@johndoe'
        self.assert_user_is_invalid()

    def test_username_can_not_be_blank(self):
        self.user.username = ''
        self.assert_user_is_invalid()
    def test_firstname_can_not_be_blank(self):
        self.user.first_name = ''
        self.assert_user_is_invalid()

    def test_username_must_be_unique(self):
        second_user = self.create_second_user()
        self.user.username = second_user.username
        self.assert_user_is_invalid()
    def test_firstname_need_not_be_unique(self):
        second_user = self.create_second_user()
        self.user.first_name = second_user.first_name
        self.assert_user_is_valid()

    def test_lastname_need_not_be_unique(self):
        second_user = self.create_second_user()
        self.user.last_name = second_user.last_name
        self.assert_user_is_valid()
    def test_lastname_must_not_be_blank(self):
        self.user.last_name = ''
        self.assert_user_is_invalid()
    def test_firstname_may_contain_50_characters(self):
        self.user.first_name = '@'*50
        self.assert_user_is_valid()
    def test_firstname_must_not_contain_over_50_characters(self):
        self.user.first_name = '@'*51
        self.assert_user_is_invalid()
    def test_lastname_may_contain_50_characters(self):
        self.user.last_name = '@'*50
        self.assert_user_is_valid()
    def test_lastname_must_not_contain_over_50_characters(self):
        self.user.last_name = '@'*51
        self.assert_user_is_invalid()
    def test_email_must_be_unique(self):
        second_user = self.create_second_user()
        self.user.email = second_user.email
        self.assert_user_is_invalid()
    def test_email_must_not_be_blank(self):
        self.user.email = ''
        self.assert_user_is_invalid()
    def test_email_must_contain_username(self):
        self.user.email = '@example.com'
        self.assert_user_is_invalid()
    def test_email_must_contain_at_symbol(self):
        self.user.email = 'johndoe.example.com'
        self.assert_user_is_invalid()
    def test_email_must_contain_domain_name(self):
        self.user.email = 'johndoe@.com'
        self.assert_user_is_invalid()
    def test_email_must_contain_domain(self):
        self.user.email = 'johndoe@example'
        self.assert_user_is_invalid()
    def test_email_must_not_contain_more_than_one_at(self):
        self.user.email = 'johndoe@@example.com'
        self.assert_user_is_invalid()
    def test_bio_may_be_blank(self):
        self.user.bio = ''
        self.assert_user_is_valid()
    def test_bio_may_contain_520_characters(self):
        self.user.bio= 'a' * 520
        self.assert_user_is_valid()
    def test_bio_may_not_contain_over_520_characters(self):
        self.user.bio= 'a' * 521
        self.assert_user_is_invalid()
    def assert_user_is_invalid(self):
        with self.assertRaises(ValidationError):
            self.user.full_clean()
    def assert_user_is_valid(self):
        try:
            self.user.full_clean()
        except(ValidationError):
            self.fail('user should be valid')

    def create_second_user(self):
       user =  User.objects.create_user(
            '@janedoe',
            first_name='Jane',
            last_name='doe',
            email='jane@example.com',
            password='Password123',
            bio='this is jane bio'
        )
       return user


