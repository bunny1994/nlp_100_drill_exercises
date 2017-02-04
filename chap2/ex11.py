#!/usr/bin/env python
# -*- coding: utf-8 -*- 

#Chuyển mỗi kí tự tab thành space

file = open('hightemp.txt', 'U')

count = 0
for f in file:
	print f.replace("\t", " ")
	
file.close()