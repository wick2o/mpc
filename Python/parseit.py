#!/usr/bin/env python

import argparse
import re

main():
  parser = argparse.ArgumentParser()
  parser.add_argument('--regex', '-r', action='store', dest='py_regex', required=True, help='Python regex code')
  parser.add_argument('--file', '-f', action='store', dest='py_file', required=True, help='file to run regex on')
  args = parser.parse_args()
  
  #test if file exists
  f = open(args.py_file, 'r')
  my_data = f.read()
  f.close()
  
  dp = re.compile(args.py_regex, re.I | re.M)
  my_res = dp.findall(my_data)
  for res in my_res:
	print res
  
  
  
  
  
if __name__ == '__main__':
  main()