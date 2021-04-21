from django import forms
from farms import models

class CreateFarmForm(forms.ModelForm):
    class Meta:
        model = models.Farm
        fields = ['farm_name']

class TelephoneCreateForm(forms.ModelForm):
    class Meta:
        model = models.Telephone
        fields = ['phonenumber']
        labels = {'phonenumber': 'Phone Number'}

class AddressCreateForm(forms.ModelForm):
    class Meta:
        model = models.Address
        fields = ['street_name', 'street_no', 'city', 'state','country']
        labels = {
            'street_name': 'Street Name',
            'street_no': 'Street No'}

class DateInput(forms.DateInput):
    input_type = "date"

    def __init__(self, **kwargs):
        kwargs["format"] = "%Y-%m-%d"
        super().__init__(**kwargs)
