#coding=utf-8

import xlsxwriter

workbook = xlsxwriter.Workbook('demo2.xlsx')
worksheet = workbook.add_worksheet()

worksheet.set_column('A:A', 20)
bold = workbook.add_format({'bold': True})

worksheet.write('A1','Hello')
worksheet.write('A2','World', bold)
worksheet.write('B2',u'中文测试', bold)

worksheet.write(2, 0, 32)
worksheet.write(3, 0, 35.5)
worksheet.write(4, 0, '=SUM(A3:A4)')


worksheet.write(2, 1, 3)
worksheet.write(3, 1, 3.34)
worksheet.write(4, 1, '=SUM(B3:B4)')

worksheet.insert_image('B6','/opt/zdh/jcp/img/python_01.png')

workbook.close()
