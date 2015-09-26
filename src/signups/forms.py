#This contains the sign up forms


from django import forms

from signups.models import SignUp

class SignUpForm(forms.ModelForm):
    class Meta:
        model = SignUp
