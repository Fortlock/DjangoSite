import xlrd
from userstatistics.models import Task, Job
from django.contrib.auth.models import User

HEADER_SKIP_COLS = 1

class Import:
	def get_header(self,sheet):
		head = []
		for col_index in range(HEADER_SKIP_COLS,sheet.ncols):
			val = sheet.cell(0, col_index).value
			if (isinstance(val, float) and round(val) == val):
				head.append(str(round(val)))
			elif (not isinstance(val, str)):
				head.append(str(val))
			else:
				head.append(val)
		return head
	#return block from fitst empty line to next empty line 
	def get_block(self,sheet, start_row_num = 0):
		if (start_row_num != 0):
			crr_val = sheet.cell_value(start_row_num,0)
			while (crr_val != u'' and start_row_num<sheet.nrows-1):
				start_row_num+=1
				crr_val = sheet.cell_value(start_row_num,0)

		rows = []
		crr_row_num = start_row_num
		crr_val = u'-'
		while(crr_val != u'' and crr_row_num<sheet.nrows-1):
			crr_row_num+=1
			row = sheet.row_values(crr_row_num)
			crr_val = row[0]
			if (crr_val!=u''):
				rows.append(row)
		end_block = not crr_row_num < sheet.nrows-1
		return end_block,crr_row_num,rows

	def import_xls(self, path):
		#open file
		wb = xlrd.open_workbook(file_contents = path.read())
		if (wb):
			sheet = wb.sheet_by_index(0)
			if (sheet):
				head = self.get_header(sheet)
				#read jobs from file
				end = False
				next_job_num = 0
				err_jobs = []
				while (not end):
					crr_job_num = next_job_num
					end,next_job_num,job_block = self.get_block(sheet, next_job_num)
					if not (Job.import_job(head,job_block,abort_if_user_not_exists = False)):
						err_jobs.append(crr_job_num)