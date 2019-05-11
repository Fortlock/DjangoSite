from django import forms

class ImportExcel(forms.Form):
	file = forms.FileField(label= "Choose excel to upload")