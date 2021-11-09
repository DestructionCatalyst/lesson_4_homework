from django import forms
from .models import Positions


class ApplyForm(forms.Form):
    choices = tuple(map(lambda pos: (pos.id, pos.name), Positions.objects.all()))

    name = forms.CharField(label='Your name', max_length=100)
    date_of_birth = forms.DateField(label='Your birth date')
    position = forms.ChoiceField(label='Desired position', choices=choices)
    phone = forms.CharField(label='Your mobile phone number', max_length=16)
    email = forms.EmailField(label='Your e-mail')


