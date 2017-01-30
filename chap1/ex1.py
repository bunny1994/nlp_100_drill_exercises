#!/usr/bin/env python
# -*- coding: utf-8 -*- 

#Từ xâu ký tự "MPyaktQrBoilk RCSahr", hãy trích xuất các ký tự ở vị trí 2,4,6,8,10,12,14,16,18,20 và kết hợp theo thứ tự đó để tạo thành 1 xâu ký tự mới (ký tự space cũng được tính, các ký tự được đánh số từ 1).

text = "MPyaktQrBoilk RCSahr"
new_text = ''

token = list(text)
for i in range(len(token)):
	if(i % 2 == 0) and (i != 0):
		new_text += token[i]

print new_text	