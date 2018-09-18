from django import forms
from .models import Post, Comment


class SearchForm(forms.Form):
    search = forms.CharField()


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','tags','body','show_to','post_status')
        widgets = {
            'body': forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent',}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
        widgets = {
          'body': forms.Textarea(attrs={'rows':2, 'cols':40,'class':'editable medium-editor-textarea postcontent',}),
        }