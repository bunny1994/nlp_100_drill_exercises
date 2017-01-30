#!/usr/bin/env python
# -*- coding: utf-8 -*- 

#Tokenize câu sau: "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
#Đưa ra danh sách gồm số ký tự alphabet trong mỗi từ theo thứ tự xuất hiện của từ đó trong câu.

import nltk

sentence = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'
tokens = nltk.word_tokenize(sentence)

print "Kí tự của câu là: " + str(tokens)
print "////////////////////////////////"

for i in range(len(tokens)):
	print "Từ '" + tokens[i] + "' có " + str(len(list(tokens[i]))) + " kí tự"