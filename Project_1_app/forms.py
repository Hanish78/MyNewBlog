from django import forms
from .models import BlogContent

 
 
# creating a form
class TestForm(forms.Form):
    NAME = forms.CharField(max_length=200)
    ROLL_NO = forms.IntegerField()
    SCHOLL_NAME = forms.CharField(max_length=200)

class ModelsDemoForm(forms.ModelForm):
    class Meta:
        # specify model to be used
        model = BlogContent
 
        # specify fields to be used
        fields = '__all__'
