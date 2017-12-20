#!/usr/bin/env python
import re,os

def  get_files(path):#获取目录下的所有文件
	return os.listdir(path)

def get_word_list(path,file):#获取所有的行
	with open(path+'/'+file) as f:
		word_list=f.readlines()
	return word_list

def count_lines(word_list):#分别数每一种行的个数
	print(word_list)
	d={'total':0,'word':0,'blank':0,'#':0}
	for line in word_list:
		d['total']=d['total']+1

		if re.match(r'^#',line):
			d['#']=d['#']+1

		elif re.match(r'^\n',line):
			d['blank']=d['blank']+1

		else:
			d['word']=d['word']+1

	return d

if __name__=='__main__':
	path='../0006'
	files=get_files(path)
	for file in files:
		word_list=get_word_list(path,file)
		d=count_lines(word_list)
		print(d)
