#!/usr/bin/env python
# -*- coding: utf-8 -*- 

#Sinh ra tập X và Y tương ứng là tập các character bi-gram từ hai xâu ký tự "paraparaparadise" và "paragraph".
#Sinh ra các tập hợp union, intersection và difference của X và Y
#Kiểm tra xem bi-gram 'se' có thuộc tập X (Y) hay không?

import nltk
from nltk import ngrams

def character_n_grams(sentence, n):
	n_character_grams = ngrams(sentence, n)
	return n_character_grams

def check_grams_in_list(grams, list):
	if grams in list:
		return "Có"
	else:
		return "Không"	

token_1 = "paraparaparadise"
token_2 = "paragraph"
bi_gram = "se"
n = 2

X = character_n_grams(token_1, n)
Y = character_n_grams(token_2, n)

X_union_Y = list(set(X).union(Y))
X_intersection_Y = list(set(X).intersection(Y))
X_difference_Y = list(set(X).difference(Y))

print X_union_Y
print "//////////////////////////////////////////////////"
print X_intersection_Y
print "//////////////////////////////////////////////////"
print X_difference_Y
print "//////////////////////////////////////////////////"
print "bi-gram 'se' " + check_grams_in_list(bi_gram, X) + "  ở trong X"
print "//////////////////////////////////////////////////"
print "bi-gram 'se' " + check_grams_in_list(bi_gram, Y) + "  ở trong Y"
print "//////////////////////////////////////////////////"