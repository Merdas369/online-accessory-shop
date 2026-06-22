from django import forms


class SearchForm(forms.Form):
    title = forms.CharField(max_length=255, widget=forms.TextInput)


class MaterialForm(forms.Form):
    gold = forms.CheckboxInput()
    silver = forms.CheckboxInput()
    bronze = forms.CheckboxInput()
