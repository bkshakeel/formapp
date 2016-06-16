from django import forms
from frmexp.models import Article

class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = ('title',)
