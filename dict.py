# -*- coding:utf8 -*-
#从语料中提取中文词，保存为一词一行的词典

import string
import re
import sys

def shell():
	if len(sys.argv)!=3 :
		print("使用方法：dict.py 输入文件名 输出文件名\n")
	else:
		create_dict(sys.argv[1],sys.argv[2])

def create_dict(filename, output_filename):
	print("打开文件: %s" % filename)
	src_data = open(filename,"r").read()
	sp_data = src_data.split()

	print("词数:",len(sp_data))
	#set_data = set(sp_data)	#去重
	#data = list(set_data)
	data=sp_data
	
	print("建立字典……")
	tmp = []
	for i in range(0,len(data)):
		if re.compile(r'\d+\-\S+').match(data[i]):  #过滤'19980101-01-001-002/m'
			continue
		else:
			pattern = u'\/[\w\[\]]+'
			p_ok_data = re.compile(pattern).sub('',data[i]) #过滤词性标注
			if re.compile(r'(\[\S+)|(\]\S+)').match(p_ok_data):#过滤专有名词标注
				#print(p_ok_data)
				p_ok_data = re.compile(r'(\]\w+\[)|(\])|(\[)').sub('',p_ok_data)
				#print(p_ok_data)
			if re.compile(r'\S*\{\S+\}').match(p_ok_data):#过滤注音
				p_ok_data = re.compile(r'\{\S*\}').sub('',p_ok_data)
			if p_ok_data.find('{')!=-1: #过滤奇怪的大括号
				p_ok_data = re.compile(r'\{').sub('',p_ok_data)
			
			tmp.append(p_ok_data+"\n")
	
	open("correct_seg_full.txt","w",encoding="utf-8").writelines(tmp)
	dict_2pass = set(tmp)	#去重
	# for i in dict_2pass:
		# if i.find('{')!=-1:
			# print(i)

	print("完成。字典词数:",len(dict_2pass)) 
	open(output_filename,'w',encoding="utf-8").writelines(dict_2pass)
	print("输出文件: %s"  % output_filename)

if __name__ == '__main__':
	shell()
