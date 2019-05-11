from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ImportExcel
from .simport import Import

# Create your views here.

def import_statistics_xls(request):
	if request.method=='POST':
		form = ImportExcel(request.POST, request.FILES)
		if form.is_valid():
			my_import = Import()
			my_import.import_xls(request.FILES['file'])
		return HttpResponseRedirect('/')
	else:
		form = ImportExcel()
		return render(request, 'import/import_statistics.html', {'form': form,})