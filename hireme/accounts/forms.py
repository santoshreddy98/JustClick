from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserChangeForm
from .models import UserProfile
from phonenumber_field.modelfields import PhoneNumberField

class RegistrationForm(UserCreationForm):
    username = forms.CharField(required=True,widget=forms.TextInput(
        attrs = {
        'class':'form-control',
        'placeholder':'Username'
        }
    ))
    first_name = forms.CharField(required=True,widget=forms.TextInput(
        attrs = {
        'class':'form-control',
        'placeholder':'Your First name'
        }
    ))
    last_name = forms.CharField(required=True,widget=forms.TextInput(
        attrs = {
        'class':'form-control',
        'placeholder':'Your Last name'
        }
    ))
    email = forms.CharField(required=True,widget=forms.EmailInput(
        attrs = {
        'class':'form-control',
        'placeholder':'Your Email Id'
        }
    ))
    password1 = forms.CharField(required=True,widget=forms.PasswordInput(
        attrs = {
        'class':'form-control',
        'placeholder':'Password'
        }
    ))
    password2 = forms.CharField(required=True,widget=forms.PasswordInput(
        attrs = {
        'class':'form-control',
        'placeholder':'Confirm Password'
        }
    ))


    class Meta:
        model = User
        fields = ('username',
                'first_name',
                'last_name',
                'email',
                'password1',
                'password2',
            )

    def save(self,commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user

class EditProfileForm(UserChangeForm):
    first_name = forms.CharField(widget = forms.TextInput(
            attrs = {
            'class' :'form-control',
            'placeholder' : "First Name"
            }
        ))
    last_name = forms.CharField(widget = forms.TextInput(
                    attrs = {
                    'class' :'form-control',
                    'placeholder' : "Last Name"
                    }
                ))
    email = forms.CharField(widget = forms.EmailInput(
                            attrs = {
                            'class' :'form-control',
                            'placeholder' : "Email Id"
                            }
                        ))
    class Meta:
        model = User
        fields = (
            'email',
            'first_name',
            'last_name',
            'password',
        )

class ProfileForm(forms.ModelForm):
    description = forms.CharField(widget = forms.TextInput(
        attrs = {
        'class' :'form-control',
        'placeholder' : "Description"
        }
        ))
    qualif = forms.CharField(widget = forms.TextInput(
        attrs = {
        'class' :'form-control',
        'placeholder' : "Qualification"
        }
        ))
    category = forms.CharField(widget = forms.TextInput(
        attrs = {
        'class' :'form-control',
        'placeholder' : "Category"
        }
        ))
    phone = PhoneNumberField()


    class Meta:
        model = UserProfile
        fields = ('description','qualif','category','phone')
