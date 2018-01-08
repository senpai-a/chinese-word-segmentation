# -*- coding:utf8 -*-
import codecs
import sys
import string

def shell():
	if len(sys.argv)!=3:
		print("使用方法：comp.py 正确分词文件名 分词输出文件名")
	else:
		correctList=open(sys.argv[1],"r",encoding="utf-8").read().split("\n")
		list=open(sys.argv[2],"r",encoding="utf-8").read().split("\n")
		comp(correctList,list)

def comp(correctList,list):
	correct = 0
	lpoint=0
	cpoint=0
	citer=0
	for w in list:
		#print(lpoint,cpoint,citer,"\n",w,correctList[citer])
		while(lpoint>cpoint and citer<len(correctList)):
			cpoint+=len(correctList[citer])
			citer+=1
		#print(lpoint,cpoint,citer,"\n",w,correctList[citer])
		#input()
		if citer==len(correctList):
			continue
		if lpoint<cpoint:
			lpoint+=len(w)
			continue
		if w==correctList[citer]:
			correct+=1
		lpoint+=len(w)
	
	print("正确结果个数：%d"%correct)
	print("全部输出结果个数：%d"%len(list))
	print("正确答案个数：%d"%len(correctList))
	
	P=correct*1.0/len(list)
	R=correct*1.0/len(correctList)
	F=2*P*R/(P+R)
	
	print("准确率P= %.3f"%P)
	print("召回率R= %.3f"%R)
	print("F测度= %.3f"%F)
	
if __name__ == "__main__":
	shell()