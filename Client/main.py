import pycurl
from   io import BytesIO
from   flask import Flask

app = Flask(__name__)

def getIP():
	buffer = BytesIO()
	c = pycurl.Curl()
	c.setopt(c.URL, 'ipinfo.io/ip')
	c.setopt(c.WRITEDATA, buffer)
	c.perform()
	c.close()
	body = buffer.getvalue()
	return body.decode('iso-8859-1').rstrip()

def main():
	print ("Iniciando cliente")
	IP = getIP()
	print (IP)

if __name__ == '__main__':
	main()
