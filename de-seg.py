# -*- coding:utf8 -*-
import codecs
import sys
import string

def main():
	if len(sys.argv)!=3:
		print("de-seg.py反分词：输入分词后的文本，输出分词前的文本。")
		print("使用方法：de-seg.py 输入文件名 输出文件名")
	else:
		list=open(sys.argv[1],"r",encoding="utf-8").read().split("\n")
		open(sys.argv[2],"w",encoding="utf-8").writelines(list)
		
if __name__ == "__main__":
	main()