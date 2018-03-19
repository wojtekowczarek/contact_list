from django import forms


class PersonCreateForm(forms.Form):
    name = forms.CharField(label='Name', max_length=16)
    surname = forms.CharField(label='Surname', max_length=16)
    description = forms.CharField(label='Description', widget=forms.Textarea)
