__author__ = 'BluePie'
import os

def readingaa():
	from test2 import checking
	name = input("Enter a username:")
	print("Brutforcing:",name)
	with open('rockyou.txt','r',encoding='ascii',errors='ignore') as f:
		i=1
		for line in f:
			checking(name,line)
			