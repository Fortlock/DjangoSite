import xlwt

class Export:
	def __init__(self, header=None, body=None):
		self.header, self.body = header, body

	def export_xls(self, stream):
		# Create workbook
		wb = xlwt.Workbook(encoding='utf-8')
		ws = wb.add_sheet('first')
		# Sheet header, first row
		row_num = 0
		font_style = xlwt.XFStyle()
		font_style.font.bold = True

		columns = self.header
		for col_num in range(len(columns)):
			ws.write(row_num, col_num, columns[col_num], font_style)

		font_style = xlwt.XFStyle()

		for row in self.body:
			row_num += 1
			for col_num in range(len(row)):
				ws.write(row_num, col_num, row[col_num], font_style)

		wb.save(stream)