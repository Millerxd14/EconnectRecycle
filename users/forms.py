from django import forms



class ProfileForm(forms.Form):
    phone_number = forms.CharField(max_length=20,required=True)
    direction = forms.CharField(max_length=100, required=True)
    person_type = forms.IntegerField(required=True)
    profile_picture = forms.ImageField(required=False)
    company_name = forms.CharField(max_length=30)
    dni = forms.CharField(max_length=20)