from django import forms

from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
import datetime #for checking renewal date range.
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.admin.widgets import FilteredSelectMultiple
    
class SelectProfileFieldsForm(forms.Form):
	user_fields = {'first_name','last_name'}
	user_other_fields = User._meta.get_fields()
	FIELD_CHOICES = []
	for f in user_other_fields:
		if f.name in user_fields:
			FIELD_CHOICES.append(['user__'+f.name,f.verbose_name])
	FIELD_CHOICES += [[f.name,f.verbose_name] for f in Profile._meta.get_fields()]

	fields_list = forms.MultipleChoiceField(widget=FilteredSelectMultiple('fields',is_stacked=False),choices=FIELD_CHOICES)

	def clean_renewal_date(self):
		data = self.cleaned_data['fields_list']
		return data

	class Media:
		css = {'all': ('/static/admin/css/widgets.css',),}
		js = ('/admin/jsi18n',)