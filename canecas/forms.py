from django import forms

class CreateCaneca(forms.Form):
    usuario = forms.CharField(min_length=4)
    name = forms.CharField(min_length=5)
    description = forms.CharField(min_length=4, max_length=30)
    mac  = forms.CharField(max_length=15)
    direction = forms.CharField(max_length=50)

    

