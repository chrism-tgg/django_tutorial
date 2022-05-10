from django import forms

class CreateNewList(forms.Form):
    # define fields
    name = forms.CharField(label="Name", max_length=200)
    check = forms.BooleanField(label="Completed", required=False)