from django import forms
from .models import Post,Product
from django.shortcuts import render


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

class ProForm(forms.ModelForm):

	class Meta:
		model = Product
		fields = ('name','code',)

