#!/usr/bin/env pyhton
import os,re
def find_keyword(file_path):
    keywords = {}
    file_name=os.path.basename(file_path)
    with open(file_name) as file:
        text=file.read()
        word_list=re.findall(r'[a-zA-Z]+',text.lower())
        for word in word_list:
            if word in keywords:
                keywords[word]+=1
            else:
                keywords[word]=1

        keywords_sorted=sorted(keywords.items(),key=lambda d : d[1])
        return file_name,keywords_sorted

file_name,results=find_keyword('./ma.py')
print(results)
