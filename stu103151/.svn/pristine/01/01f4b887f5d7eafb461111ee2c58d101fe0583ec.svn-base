from django import forms
from store import models

class BookForm(forms.Form):
    name = forms.CharField(max_length=10)
    pulication_date = forms.DateField()

class BookModelForm(forms.ModelForm):
    class Meta:
        model = models.Book
        exclude = ()
