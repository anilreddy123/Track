from django import forms
from django.forms import ModelForm, CharField
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.contrib.auth.models import User
from. models import *

class AddUserForm(forms.Form):
    username = forms.RegexField(regex=r'^\w+$', widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=("User Name"), error_messages={ 'invalid': ("This value must contain only letters, numbers and underscores.") })
    password1 = forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True, max_length=30, render_value=False)), label=("Password"))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True, max_length=30, render_value=False)), label=("Password (again)"))


    def clean_username(self):
        try:
            user = User.objects.get(username__iexact=self.cleaned_data['username'])
        except User.DoesNotExist:
            return self.cleaned_data['username']
        raise forms.ValidationError(("The username already exists. Please try another one."))

    def clean(self):
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                raise forms.ValidationError(("The two password fields did not match."))
        return self.cleaned_data




class UpdateProfile(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name')

    def clean_username(self):
        try:
            user = User.objects.get(username__iexact=self.cleaned_data['username'])
        except User.DoesNotExist:
            return self.cleaned_data['username']
        raise forms.ValidationError(("The username already exists. Please try another one."))



class Mobile_regForm(forms.ModelForm):
    class Meta:
        model = MobileReg
        fields = '__all__'



class AddDeviceForm(forms.ModelForm):
    class Meta:
        model = AddDevice
        fields = '__all__'
'''
class waypointForm(forms.Form):
    def __init__(self, user, *args, **kwargs):
        super(waypointForm, self).__init__(*args, **kwargs)
        self.fields['waypoints'] = forms.ChoiceField(
            choices=[(o.id, str(o)) for o in Waypoint.objects.filter(user=user)]
)'''
