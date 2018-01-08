# -*- coding:utf8 -*-
import codecs
import string
import re
import sys

def load_dict(filename):  
    f = open(filename,'r',encoding="utf-8").read()  
    maxLen = 1  
    dict=f.split("\n")
    for i in dict:  
        if len(i)>maxLen:  
            maxLen=len(i)  
  
    return dict,maxLen;  
  
#分词 返回分好的列表
def maxlen_segmentation(dict,maxLen,sentence,foreward=True):
	wordList=[]  #结果
	#print("calling seg function: maxLen %d"%maxLen)
	cycle=len(sentence)/100
	i=0
	j=0
	while(len(sentence)>0):
		n = len(sentence)
		
		if i>cycle :
			i=0
			j+=1
			print("%d%% 完成"%j)
		
		if foreward:
			word=sentence[0:maxLen]
		else:
			word=sentence[n-maxLen:n]

		found=False;   #是否找到词  
  
		while((not found) and (len(word)>0)):
			if(word in dict):  #命中
				wordList.append(word+'\n')
				#print("命中 %s"%word)
				i+=len(word)
				if foreward:
					sentence=sentence[len(word):n]#后移
				else:
					sentence=sentence[0:n-len(word)]#前移
					#print("下一个 %s"%sentence)
					#input();
				found=True;
			else:  
                #当词长为1时,强行命中  
				if(len(word)==1):  
					wordList.append(word+'\n')
					#print("单字 %s"%word)
					i+=len(word)					
					if foreward:
						sentence=sentence[len(word):n]#后移
					else:
						sentence=sentence[0:n-len(word)]#前移
						#print("下一个 %s"%sentence)
						#input();
					found=True; 
				else:
					if foreward:
						word=word[0:len(word)-1]
					else:
						word=word[1:len(word)]
						#print(word)

	return wordList  
  
def main():
	if len(sys.argv)!=3:
		print('用法：seg.py 词典文件名 输入文件名')
		return
		
	dict,maxLen=load_dict(sys.argv[1])
	strIn = open(sys.argv[2],encoding="utf-8").read()
	
	print("开始分词...\n")
	
	f_result=maxlen_segmentation(dict,maxLen,strIn,True)	
	b_result=maxlen_segmentation(dict,maxLen,strIn,False)
	print('前向最大匹配分词：%d个词'%len(f_result))
	print('后向最大匹配分词：%d个词'%len(b_result))
	
	open('foreward.txt','w',encoding="utf-8").writelines(f_result)
	open('backward.txt','w',encoding="utf-8").writelines(b_result[::-1])
	print('结果已保存在foreward.txt backward.txt')
  
if __name__ == '__main__':  
	main()