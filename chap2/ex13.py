#!/usr/bin/env python
# -*- coding: utf-8 -*- 

#Kết hợp nội dung trong 2 file col1.txt và col2.txt để tạo thành một file mới có nội dung giống với cột 1 và cột 2 trong file ban đầu (các cột cách nhau bởi ký tự tab). Sử dụng lệnh paste để thực hiện bài tập và xác nhận kết quả của chương trình bạn viết.

col_1 = open('col_1.txt', 'U')
col_2 = open('col_2.txt', 'U')
new_hightemp = open('new_hightemp.txt', 'w')
arr = []
n = 0

for i in col_1:
	print i
	arr.append(i)

for i in col_2:
	arr[n] += '\t' + i
	new_hightemp.write(arr[n])
	new_hightemp.write("\n")
	n += 1 	
