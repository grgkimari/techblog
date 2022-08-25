from django import  forms
from .models import Post,  Category

categories= Category.objects.all().values_list('name', 'name')

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        widgets = {
            'category' : forms.Select(choices = categories, attrs={'class' : 'form-control',}),
            'title' : forms.TextInput(attrs={'class' : 'form-control',}),
            'author' : forms.Select(attrs={'class' : 'form-control',}),
            'body' : forms.Textarea(attrs={'class' : 'form-control',}),
            
        }