import httplib
import boto

httpclient = httplib.HTTPConnection("ec2-52-30-7-5.eu-west-1.compute.amazonaws.com", 81);
httpclient.connect()

httpclient.request('GET', '/key');
response = httpclient.getresponse();

for item in response.read().split(':'):
	print item

print boto.Version
