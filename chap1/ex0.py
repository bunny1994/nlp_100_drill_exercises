#!/usr/bin/env python
# -*- coding: utf-8 -*- 

#Hãy đảo ngược xâu ký tự "stressed" (theo thứ tự từ cuối xâu đến đầu xâu ký tự).

text = "stressed"
reversed_text = ''

token = list(text)
for i in range(len(token)-1, -1, -1):
	reversed_text += token[i]

print reversed_text	