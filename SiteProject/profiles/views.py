from django.shortcuts import render




# Create your views here.

def index(request):
    return render(
        request,
        'profiles/index.html',
    )

from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Profile
import xlwt
from .forms import SelectProfileFieldsForm

def export_users_xls(request):
	if request.method=='POST':
		form = SelectProfileFieldsForm(request.POST)
		if form.is_valid():
			fields = form.cleaned_data['fields_list']
			response = HttpResponse(content_type='application/ms-excel')
			response['Content-Disposition'] = 'attachment; filename="users.xls"'

			wb = xlwt.Workbook(encoding='utf-8')
			ws = wb.add_sheet('Profiles')

			# Sheet header, first row
			row_num = 0

			font_style = xlwt.XFStyle()
			font_style.font.bold = True

			columns = fields

			for col_num in range(len(columns)):
				ws.write(row_num, col_num, columns[col_num], font_style)

			# Sheet body, remaining rows
			font_style = xlwt.XFStyle()

			rows = Profile.objects.all().values_list(*fields)
			for row in rows:
				row_num += 1
				for col_num in range(len(row)):
					ws.write(row_num, col_num, row[col_num], font_style)

			wb.save(response)
			return response
	else:
		form = SelectProfileFieldsForm()
		return render(request, 'profiles/export_profiles.html', {'form': form,})