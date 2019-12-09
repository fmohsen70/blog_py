from django import forms

from .models import Post,Product

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

class ProForm(forms.ModelForm):

	class Meta:
		model = Product
		fields = ('name','code',)