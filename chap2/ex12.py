#!/usr/bin/env python
# -*- coding: utf-8 -*- 

#Trích xuất nội dung trong cột 1, cột 2 và lưu vào các file tương ứng: col1.txt và col2.txt. Thử thực hiện công việc chỉ dùng lệnh cut trong unix.

file = open('hightemp.txt', 'U')

col_1 = open('col_1.txt', 'w')
col_2 = open('col_2.txt', 'w')

for f in file:
	line = f.split("\t")
	col_1.write(line[0])
	col_1.write("\n")
	
	col_2.write(line[0])
	col_2.write("\n")

file.close()