from django import forms
from .models import *


class RatingForm(forms.ModelForm):
	class Meta:
		model = NewCourse
		fields = ['Course_name','Course_star_rating','Course_comments']
		widgets = {
						
						'Course_name' : forms.TextInput(attrs={'class':'form-control'}),
						'Course_star_rating': forms.TextInput(attrs={'class':'form-control'}),
						'Course_comments': forms.TextInput(attrs={'class':'form-control'}),
					}


class ReviewForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ("comment","rating")