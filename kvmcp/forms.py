from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _


class BootstrapAuthenticationForm(AuthenticationForm):
    username = forms.CharField(max_length=20, label=_("Имя пользователя"), widget=forms.TextInput({
                                                                    'class': 'form-control',
                                                                    'placeholder': 'Username'}))
    password = forms.CharField(label=_("Пароль"), widget=forms.PasswordInput({
                                                    'class': 'form-control',
                                                    'placeholder': 'Password'}))

class ChoiceKvm(forms.Form):
    ch_kvm = forms.CharField(max_length=10, required=False)