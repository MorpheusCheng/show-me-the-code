#!/usr/bin/env python
import os
from PIL import Image

def get_file(path):
	return os.listdir(path)

def set_picure(path,file):
	i=0
	for f in file:
		#print(f)
		with Image.open(path+'/'+f) as im:
			im.thumbnail((1136,640))#注意这里是tuple
			im.save(path+'/'+str(i)+'.jpg','jpeg')
			i=i+1

if __name__=='__main__':
	path='/home/cheng/Pictures'
	file=get_file(path)
	set_picure(path,file)
