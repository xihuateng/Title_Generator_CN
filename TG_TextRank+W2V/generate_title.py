#-*- encoding:utf-8 -*-
''' USED sgns.sogou.word 
https://github.com/Embedding/Chinese-Word-Vectors
'''
import os, sys
import json
import numpy as np
sys.path.append(sys.path[0]+'/textrank/')
from TextRank4Sentence import TextRank4Sentence

content_path = '/'.join(sys.path[0].split('/')[0:-1]) + '/validation/content.txt'
title_trw2v_path = '/'.join(sys.path[0].split('/')[0:-1]) + '/validation/title_trw2v.txt'


def get_shorter_title():
    for item in tr4s.get_key_sentences(num=3,sentence_min_len = 5):
        if len(item['sentence']) < 50:
            return item['sentence']
    return "最新新闻报道"


tr4s = TextRank4Sentence()
cnt = 0
title = []

for line in open(content_path,"r",encoding="utf-8"):

    tr4s.analyze(text=line, lower=True, source = 'all_filters')

    title_tmp = tr4s.get_key_sentences(num=1,sentence_min_len = 5)
    if len(title_tmp) < 1:
        title.append('最新新闻报道')
    else:
        if len(title_tmp[0]['sentence']) > 50:
            title.append(get_shorter_title())
        else:
            title.append(title_tmp[0]['sentence'])
    
    cnt += 1
    if cnt % 50 == 0:
        print(f"{cnt} title have been generated by textrank+w2v_model.")

f = open(title_trw2v_path,'a+',encoding='utf-8')
for item in title:
    f.write(item+'\n')
f.close()
