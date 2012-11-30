#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import socket
import argparse

def valid_ip(address):
	try:
		socket.inet_aton(address)
		return True
	except:
		return False
		
		
def setup():
	parser = argparse.ArgumentParser()
	parser.add_argument('-f', '--file', action='store', dest='file', required=True,  help='File with ips, one per line')

	global args
	args = parser.parse_args()
	
def main():
	setup()
	
	ipaddresses = []
	valid = []
	notvalid = []
	
	ip_file = open(args.file,'r')
	ip_read = ip_file.readlines()
	ip_read = [item.rstrip() for item in ip_read]
	for ip in ip_read:
		if not ip.startswith('#'): #ignore comments
			ipaddresses.append(ip)
	ip_file.close()
	
	for ip in ipaddresses:
		res = valid_ip(ip)
		if res == True:
			valid.append(ip)
		else:
			notvalid.append(ip)
			
	v_ips = open('out_valid.txt', 'wb')
	v_ips.write('\n'.join(valid))
	v_ips.close()
	
	nv_ips = open('out_notvalid.txt', 'wb')
	nv_ips.write('\n'.join(notvalid))
	nv_ips.close()
	
	print 'completed'
	sys.exit()



if __name__ == "__main__":
	main()