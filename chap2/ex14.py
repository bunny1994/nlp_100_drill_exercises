#!/usr/bin/env python
# -*- coding: utf-8 -*- 

#Viết chương trình trích xuất ra N hàng đầu tiên của file. Biến số dạng dòng lệnh là số tự nhiên N. Sử dụng lệnh head trong unix để thực hiện công việc.

import sys 
file = open('hightemp.txt', 'U')

n = str(sys.argv[1])
i = 0

for f in file:
	if i < int(n):
		print f
		i += 1

file.close()