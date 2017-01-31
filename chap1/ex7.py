#!/usr/bin/env python
# -*- coding: utf-8 -*- 

#Viết hàm số nhận vào 3 biến x, y, z và trả về xâu ký tự "y vào lúc x giờ là z" Sinh ra kết quả với các giá trị x, y, z sau đây x="12" y="Nhiệt độ" z=22.4
#python ex7.py 12 'Nhiệt độ' 22.4
import sys

x = str(sys.argv[1])
y = str(sys.argv[2])
z = str(sys.argv[3])

text = y + " vào lúc " + x + " giờ là " + z
print text