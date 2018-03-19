from django import forms


class PersonCreateForm(forms.Form):
    name = forms.CharField(label='Name', max_length=16)
    surname = forms.CharField(label='Surname', max_length=16)
    description = forms.CharField(label='Description', widget=forms.Textarea)


class AddressCreateForm(forms.Form):
    city = forms.CharField(label='City', max_length=32)
    street = forms.CharField(label='Street', max_length=32)
    house = forms.IntegerField(label='House Number')
    flat = forms.IntegerField(label='Flat Number')


class TelephoneCreateForm(forms.Form):
    number = forms.CharField(label='Number', max_length=12)
    type = forms.CharField(label='type', max_length=32)


class EmailCreateForm(forms.Form):
    email = forms.CharField(label='email', max_length=64)
    type = forms.CharField(label='type', max_length=32)