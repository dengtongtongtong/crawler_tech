import urllib2

def scratch_facebook(url):
	try:
		request = urllib2.Request(url)
		response = urllib2.urlopen(request)
		#response = urllib2.urlopen(request,timeout=1)
		print response.read()
	except Exception as e:
		print e


def scratch_baidu(url):
	try:
		request = urllib2.Request(url)
		request.set_proxy('127.0.0.1:8888','http')
		request.add_header('User-Agent','Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1')
		response = urllib2.urlopen(request)
		print response.geturl(),response.getcode(),response.info()
	except Exception as e:
		print e

if __name__=='__main__':
	scratch_baidu('http://www.baidu.com')
	#scratch_facebook('http://www.facebook.com')
	
