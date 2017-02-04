#!/usr/bin/env python
# -*- coding: utf-8 -*- 

#Cho đầu vào là một câu tiếng Anh bao gồm các word ngăn cách nhau bằng ký tự space. Viết chương trình thực hiện việc sau:

#Với mỗi word, giữ nguyên ký tự đầu và ký tự cuối, đảo thứ tự một cách ngẫu nhiên các ký tự còn lại của (tất nhiên các word có ít hơn 4 ký tự thì không cần làm gì)
#Cho trước một câu tiếng Anh hợp lệ, ví dụ "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind .", chạy chương trình đã viết để đưa ra kết quả.

from random import shuffle

sentence = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."

token = sentence.split(" ")
new_sentence = ""

for i in range(len(token)):
	if len(token[i]) >= 4:
		x = list(token[i][1:len(token[i]) -1])
		shuffle(x)
		
		new_token = token[i][0]

		for j in xrange(len(x)):
			new_token += x[j]

		new_token += token[i][len(token[i]) -1] + " "

		new_sentence += new_token
	else:
		new_sentence += token[i] + " "

print new_sentence
			