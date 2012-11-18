#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import argparse
import Queue
import signal
import time
from threading import Thread, activeCount, Lock, current_thread
from subprocess import call

__author__  = ''
__license__ = 'BSD (3-Clause)'
__version__ = '0'
__date__ = ''
__maintainer__ = 'WiK'
__email__ = 'wick2o@gmail.com'
__status__ = 'Beta'

ipaddresses = []
queue = Queue.Queue()
sigint = False

def logo():
	#ASCII-art of some kind of logo?
	pass

def load_ipaddresses():
	if not os.path.exists(args.iplist):
		print 'The supplied file (%s) does not exists!' % (args.iplist)
		sys.exit(0)
		
	ip_file = open(args.iplist, 'r')
	ip_read = ip_file.readlines()
	ip_read = [item.rstrip() for item in ip_read]
	for ip in ip_read:
		if not ip.startswith('#'): #ignore comments
			ipaddresses.append(ip)
			
def run_process(ip):
	#print 'Looking up %s' % (ip)
	url = 'http://%s' % (ip)
	output = '%s.txt' % (ip)
	call(["wget", "-t", "1", "-T", "2", url, "-O", output])
	
	fs = os.path.getsize(output)
	if fs == 0:
		os.remove(output)
	
def process_handler(ipaddresses):
	if args.threads > 1:
		threads = []
		for ip in ipaddresses:
			queue.put(ip)
		progress_lock = Lock()
		
		while not queue.empty() and not sigint:
			if args.threads >= activeCount() and not sigint:
				ip = queue.get()
				try:
					# setup thread to run process
					t = Thread(target=run_process,args=(ip,))
					t.daemon = True
					threads.append(t)
					t.start()
				finally:
					progress_lock.acquire()
					try:
						#run a progress bar here
						pass
					finally:
						progress_lock.release()
					queue.task_done()
		while activeCount() > 1:
			time.sleep(0.1)
		for thread in threads:
			thread.join()
			
		queue.join()
	else:
		for ip in ipaddresses:
			run_process(ip)
	return
					
	
def signal_handler(signal, frame):
	#handles ctrl+c events
	global sigint
	sigint = True
	
	print ' Ctrl+C detected... exiting...\n'
	sys.exit(1)
	
def setup():
	parser = argparse.ArgumentParser()
	parser.add_argument('-t', '--threads', action='store', dest='threads', default=0, type=int, help='Enable threading. Specifiy max # of threads')
	parser.add_argument('-i', '--iplist', action='store', dest='iplist', help='Location of iplist FILE (1 per line)')
	global args
	args = parser.parse_args()
	
def main():
	logo()
	setup()
	load_ipaddresses()
	process_handler(ipaddresses)
	sys.exit()
	
if __name__ == "__main__":
	signal.signal(signal.SIGINT, signal_handler)
	main()