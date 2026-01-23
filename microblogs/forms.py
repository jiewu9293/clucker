from django import forms
from django.core.validators import RegexValidator

from .models import User
class SignUpForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username','email','bio']
    new_password = forms.CharField(label='Password',
                                   widget=forms.PasswordInput,
                                   validators=[
                                       RegexValidator(
                                       regex='^(?=.*[A-Z])(?=.*[a-z])(?=.*\d).*$',
                                       message='password must contain uppercase character，a lowercase character'
                                               'and a number'
                                   )
                                   ]
                                   )
    password_confirmation = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    def clean(self):
        super().clean()
        new_password = self.cleaned_data.get('new_password')
        password_confirmation = self.cleaned_data.get('password_confirmation')
        if new_password != password_confirmation:
            self.add_error('password_confirmation', 'Password confirmation must match')


    def save(self):
        super().save(commit=False)
        user = User.objects.create_user(
            self.cleaned_data.get('username'),
            email=self.cleaned_data.get('email'),
            first_name=self.cleaned_data.get('first_name'),
            last_name=self.cleaned_data.get('last_name'),
            bio=self.cleaned_data.get('bio'),
            password=self.cleaned_data.get('new_password')
        )
        return user

class LogInForm(forms.Form):
    username = forms.CharField(label='Username',)
    password = forms.CharField(label='Password',widget=forms.PasswordInput)











