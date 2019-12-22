from django import forms
from .models import Post,Product,Category
from django.shortcuts import render


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

class ProForm(forms.ModelForm):

	class Meta:
		model = Product		
		fields = ('name','code','category')
		reoccurrance = forms.ChoiceField(label="Reoccurance", choices=(),
                                   widget=forms.Select(attrs={'class':'selector'}))
	def __init__(self):
	    super(ProForm, self).__init__()
	    choices = []
	    for pt in Category.objects.all():
	      choices.append((pt.id, pt.name))
	    self.fields['category'].choices = choices



