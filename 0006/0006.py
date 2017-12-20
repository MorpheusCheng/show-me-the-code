#!/usr/bin/env python
import os,re
from collections import Counter

def get_file(path):
	return os.listdir(path)

def  get_most_words(path,file):
	with open(path+'/'+file) as f:
		text=f.read()
		word_list=re.findall(r'\w+',text.lower())
		return Counter(word_list).most_common(1)#使用Counter真的很方便

if __name__=='__main__':
	path='/home/cheng/Documents/test'
	files=get_file(path)
	for f in files:
		print(get_most_words(path,f))