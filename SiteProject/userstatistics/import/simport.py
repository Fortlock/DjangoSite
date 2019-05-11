import xlrd
from userstatistics.models import Task, Job
from django.contrib.auth.models import User

HEADER_SKIP_COLS = 1

class Import:
	def import_xls(self, path):
		#open file
		wb = xlrd.open_workbook(file_contents = path.read())
		if (wb):
			sheet = wb.sheet_by_index(0)
			if (sheet):
				#read header
				head = []
				for col_index in range(HEADER_SKIP_COLS,sheet.ncols):
					val = sheet.cell(0, col_index).value
					if (isinstance(val, float) and round(val) == val):
						head.append(str(round(val)))
					elif (not isinstance(val, str)):
						head.append(str(val))
					else:
						head.append(val)
				#create tasks if not exist
				tasks = []
				for col in head:
					tasks.append(Task.objects.get_or_create(name = col)[0])
				
				for row_num in range(1,sheet.nrows):
					row = sheet.row_values(row_num)
					user_exist = False
					if (row[0] != u'' and isinstance(row[0],str)):
						if ('crr_job' not in locals()):
							crr_job = Job.objects.create(year = 2019) #TODO insert year
						#try get user
						names = row[0].split()
						while(len(names)<3):
							names.append(u'')
						try:
							crr_usr = User.objects.get(first_name = names[1], last_name = names[0], profile__patronymic = names[2])
							user_exist = True
						except DoesNotExist:
							user_exist = False


		return