#!/usr/bin/env python
# -*- coding: utf-8 -*- 

#Đếm số dòng trong file. Xác nhận kết quả bằng lệnh wc trong unix.

file = open('hightemp.txt', 'U')

count = 0
for f in file:
	count += 1
	
print count	