from django import forms



class ProfileForm(forms.Form):
    phone_number = forms.CharField(max_length=20,required=True)
    direction = forms.CharField(max_length=100, required=True)
    picture = forms.ImageField()