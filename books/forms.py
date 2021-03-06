from django import forms
from books.models import Books,UserProfile
from django.contrib.auth.models import User

class BookForm(forms.ModelForm):
	title = forms.CharField(max_length=100,help_text="The Name Of the book.")
	author = forms.CharField(max_length=100,help_text="The name of the author.")
	pb_date = forms.DateTimeField(help_text ="The Publication date.")
	description = forms.CharField(max_length=1000,help_text ="Details about the book.")
	
	class Meta:
		model = Books
		fields = ('title','author','pb_date','description',)
	
class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())

	class Meta:
		model = User
		fields = ('username','email','password')

