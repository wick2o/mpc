#!/usr/bin/python

import argparse
import sys
import os
import re

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('-f', '--file', action='store', dest='mod_file', help='file to modify')
	args = parser.parse_args()
  
	if os.path.exists(args.mod_file):
		f = open(args.mod_file,"r")
		file_content = f.readlines()
		f.close
		xml = []
		for line in file_content:
			xml.append(line)
			
		for idx,itm in enumerate(xml):
			if itm.strip() == "<severity>1</severity>":
			  xml[idx - 2] = ""
			  xml[idx - 1] = ""
			  xml[idx] = ""
			  xml[idx + 1] = ""
			  xml[idx + 2] = ""
			  xml[idx + 3] = ""
			  xml[idx + 4] = ""
		
		f = open(args.mod_file,"w")
		f.write("".join(xml))
		f.close()
			
if __name__ == '__main__':
	main()
    
