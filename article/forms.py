from django import forms
from .models import Berita

# class LoginForm(forms.ModelForm):
#     # username = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'placeholder':'Username'}))
#     # password = forms.CharField(max_length=15, widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))

#     class Meta:
#         model = Berita
#         fields = ('nim', 'password_SIA')