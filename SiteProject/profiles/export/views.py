from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from profiles.models import Profile, Group
from .forms import SelectProfileFieldsForm
from .export import Export
from django.contrib.auth.decorators import login_required, permission_required

# Create your views here.

USER_REQUIRED_FIELDS = {'first_name','last_name'}

@login_required
@permission_required('can_export_group', login_url='/login/')
def export_users_xls(request):
	user_fields = User._meta.get_fields()
	profile_fields = Profile._meta.get_fields()
	fields = []
	for f in user_fields:
		if f.name in USER_REQUIRED_FIELDS:
			fields.append(['user__'+f.name,f.verbose_name])
	fields += [[f.name,f.verbose_name] for f in profile_fields]

	crr_user = request.user
	groups = Group.objects.filter(leader = crr_user)

	if request.method=='POST':
		form = SelectProfileFieldsForm(request.POST, group_choices = groups, field_choices = fields)
		if form.is_valid():
			my_header = form.cleaned_data['fields_list']
			my_body = Profile.objects.filter(group__in = groups).values_list(*my_header)

			response = HttpResponse(content_type='application/ms-excel')
			response['Content-Disposition'] = 'attachment; filename="users.xls"'

			my_export = Export(header = my_header,body = my_body)
			my_export.export_xls(response)
			
			return response
	else:
		form = SelectProfileFieldsForm(group_choices= groups, field_choices = fields)
		return render(request, 'export/export_profiles.html', {'form': form,})
