#!/usr/bin/env python
# -*- coding: utf-8 -*- 

#Viết chương trình trích xuất ra N hàng cuối cùng của file. Chương trình nhận đầu vào từ dòng lệnh là số tự nhiên N. Sử dụng lệnh tail trong unix để thực hiện công việc.

import sys 
file = open('hightemp.txt', 'U')

n = str(sys.argv[1])
count = 0
for f in file:
	count += 1

for ft in file:
	if count > (count - int(n)):
		print ft

file.close()