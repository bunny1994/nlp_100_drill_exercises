#!/usr/bin/env python
# -*- coding: utf-8 -*- 

#Viết hàm sinh ra tất cả các n-gram từ một dãy cho trước (xâu ký tự hoặc danh sách).

#Sử dụng hàm đã viết, sinh ra word bi-gram và character bi-gram từ câu sau: "I am an NLPer"
import nltk
from nltk import ngrams

def word_n_grams(sentence, n):
	n_word_grams = ngrams(nltk.word_tokenize(sentence), n)
	for grams in n_word_grams:
  		print grams

def character_n_grams(sentence, n):
	n_character_grams = ngrams(sentence, n)
	for grams in n_character_grams:
  		print grams  		

sentence = "I am an NLPer"
n = 2

print "Word bi-gram:"
word_n_grams(sentence, n)
print "//////////////////////////////////////////////////////////////"
print "Character bi-gram:"
character_n_grams(sentence, n)