#!/usr/bin/env python
# -*- coding: utf-8 -*- 

#Tokenize câu sau: "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
#Lấy ra ký tự đầu tiên của các từ ở vị trí 1, 5, 6, 7, 8, 9, 15, 16, 19; với các từ còn lại lấy ra 2 ký tự đầu tiên. Tạo ra một map từ các xâu ký tự được trích ra tới vị trí của từ trong câu.

import nltk

sentence = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."

tokens = nltk.word_tokenize(sentence)

keys = [1, 5, 6, 7, 8, 9, 15, 16, 19]
char_dict = {}

for i in xrange(len(tokens)):
	if ((i+1) in keys):
		char_dict[list(tokens[i])[0]] = i+1
	else:
		try:
			char_dict[list(tokens[i])[0] + list(tokens[i])[1]] = i+1
		except Exception, e:
			char_dict[list(tokens[i])[0]] = i+1

print tokens
print "///////////////////"
print char_dict		