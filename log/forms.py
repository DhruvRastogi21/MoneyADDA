from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Transaction
from .models import CURRENCY_CHOICES


# If you don't do this you cannot use Bootstrap CSS
class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", max_length=30,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'}))
    password = forms.CharField(label="Password", max_length=30,
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'name': 'password'}))

class TransactionForm(forms.ModelForm):


    class Meta:
        model=Transaction
        fields=['username_of_recipient','amount','currency']

class SignUpForm(UserCreationForm):
    date_of_birth = forms.DateField(widget=forms.DateInput(format="YYYY-MM-DD"),help_text='Required. Format: YYYY/MM/DD')
    currency=forms.ChoiceField(widget=forms.Select,choices=CURRENCY_CHOICES)

    class Meta:
        model = User
        fields = ('username','first_name','last_name', 'date_of_birth', 'password1', 'password2','currency')