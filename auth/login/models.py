from django import forms
from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
	user = models.OneToOneField(User)
	web = models.URLField(blank=True)
	#pic = models.ImageField()
	def __unicode__(self):
		return self.user.username

class UserForm(forms.ModelForm):
	password= forms.CharField(widget=forms.PasswordInput())
	class Meta:
		model = User
		fields=('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
	class Meta:
		model=UserProfile
		fields=('web',)
