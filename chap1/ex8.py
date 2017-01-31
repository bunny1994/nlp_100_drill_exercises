#!/usr/bin/env python
# -*- coding: utf-8 -*- 

#Nếu là ký tự tiếng Anh ở dạng thường (lower-case characters) thì chuyển thành ký tự có mã là (219 - mã ký tự).
#Các ký tự khác giữ nguyên.

def cifer(token):
	encode_token = ""
	for i in token:
		if i.islower():
			encode_token += "(219 - " + str(ord(i)) + ")"
		else:
			encode_token += i
	print encode_token

token = 'dsdasdada'
cifer(token)