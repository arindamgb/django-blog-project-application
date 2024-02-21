from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django.urls import reverse
from app_login.models import UserProfile
from django.forms import ModelForm


class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="Email", required=True)
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class UserProfileChange(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password'].help_text = (
            "Raw passwords are not stored, so there is no way to see this user’s password, but you can change the password using <a href='{}'>this form</a>."
        ).format(reverse("app_login:pass_change"))


class ProfilePic(ModelForm):
    class Meta:
        model = UserProfile
        fields = '__all__'
        #fields = ['profile_pic', ]
        exclude = ['user', ]
