#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2
import re
import argparse

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('-f', '--file', action='store', dest='file', required=True,  help='File with ips, one per line')
	args = parser.parse_args()
	
	ipaddresses = []

	lf_file = open('output.txt', 'wb')
	
	ip_file = open(args.file,'r')
	ip_read = ip_file.readlines()
	ip_read = [item.rstrip() for item in ip_read]
	for ip in ip_read:
		if not ip.startswith('#'): #ignore comments
			ipaddresses.append(ip)
	ip_file.close()

	for ip in ipaddresses:
		try:
			url = 'http://%s' % (ip)
			print 'checking %s' % (ip)
			page = urllib2.urlopen(url)
			page = page.read()
			links = re.findall(r"<a.*?\s*href=\"(.*?)\".*?>(.*?)</a>", page)
			for link in links:
				if link[0].startswith('/'):
					print 'http://%s%s' % (ip,link[0])
					lf_file.writelines('http://%s%s\n' % (ip,link[0]))
					
				else:
					print '%s\n' % (link[0])
					lf_file.writelines('%s\n' % (link[0]))
		except (urllib2.HTTPError, urllib2.URLError) as err:
			pass
				
	lf_file.close()
	
	
if __name__ == "__main__":
	main()
