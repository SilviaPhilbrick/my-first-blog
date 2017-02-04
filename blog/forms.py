from django import forms
from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',) #what will show
        #this defines which model (Post) should be used to create the class Form
