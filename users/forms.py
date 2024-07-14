from django import forms

from .models import CustomUser, Profile


class RegisterForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input', 'placeholder': 'Enter password'}), min_length=6)
	password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input', 'placeholder': 'Repeat password'}))

	class Meta:
		model = CustomUser
		exclude = ['is_staff']
		widgets = {
			'username': forms.TextInput(attrs={'class': 'input', 'placeholder': 'Enter username'}),
			'email': forms.TextInput(attrs={'class': 'input', 'placeholder': 'Enter email'}),
		}

	def clean_password2(self):
		cd = self.cleaned_data
		if cd['password'] != cd ['password2']:
			raise forms.ValidationError('Password don\'t match')
		return cd['password2']


class LoginForm(forms.Form):
	email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Enter email'}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input', 'placeholder': 'Enter password'}))


class ProfileForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'input-profile', 'placeholder': 'Enter username'}))

    class Meta:
        model = Profile
        fields = ['username']