from django_recaptcha.fields import ReCaptchaField
from django import forms


class EmailForm(forms.Form):
    email = forms.EmailField()
    captcha = ReCaptchaField()
