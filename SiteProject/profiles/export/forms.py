from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple
    
class SelectProfileFieldsForm(forms.Form):
	group_choice = forms.ModelChoiceField(queryset=None)
	fields_list = forms.MultipleChoiceField(widget=FilteredSelectMultiple('fields',is_stacked=False))

	def __init__(self, *args, **kwargs):
		groups = kwargs.pop('group_choices', None)
		fields = kwargs.pop('field_choices', None)
		super(SelectProfileFieldsForm, self).__init__(*args, **kwargs)

		self.fields['group_choice'].queryset = groups
		self.fields['fields_list'].choices = fields

	class Media:
		css = {'all': ('/static/admin/css/widgets.css',),}
		js = ('/admin/jsi18n',)
