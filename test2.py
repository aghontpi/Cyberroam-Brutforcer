__author__ = 'BluePie'
import urllib.request
import urllib

def checking(name,pword):
	url="http://172.16.10.9/login.xml"
	#"mode=191&username=" + encodeURIComponent(UserValue) + "&password=" + encodeURIComponent(document.frmHTTPClientLogin.password.value) 
	#+ "&a=" + (new Date).getTime() + producttype;
	reqdata={'mode':191,
			'username':name,
			'password':pword,}
	reqdata=encode(reqdata)
	print ('-'*80)
	print ('-'*80)
	print("trying:"+ name)
	print ('{0}{1}'.format(url,reqdata))
	while 1:
		try:
			xmlres = urllib.request.urlopen(url,data=reqdata)
			break
		except Exception as e:
			print (e)
	return xmlres.read
	#data should be a buffer in the standard application/x-www-form-urlencoded format.
	#The urllib.parse.urlencode() function takes a mapping or sequence of 2-tuples and returns an ASCII text string in this format.
	#It should be encoded to bytes before being used as the data parameter.
def encode(con):
	return (urllib.parse.urlencode(con)).encode('UTF-8')
	
if __name__ == '__main__':
   print('-'*80)
   print('author:'+__author__)
   print("Version:0.40")
   password=uname="ts012"
   test=checking(uname,password)

