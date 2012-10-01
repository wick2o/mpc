#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import argparse


alphanum = [ '21','22','23','24','25','26','27',
             '28','29','2A','2B','2C','2D','2E','2F',
             '30','31','32','33','34','35','36','37',
             '38','39','3A','3B','3C','3D','3E','3F',
             '40','41','42','43','44','45','46','47',
             '48','49','4A','4B','4C','4D','4E','4F',
             '50','51','52','53','54','55','56','57',
             '58','59','5A','5B','5C','5D','5E','5F',
             '60','61','62','63','64','65','66','67',
             '68','69','6A','6B','6C','6D','6E','6F',
             '70','71','72','73','74','75','76','77',
             '78','79','7A','7B','7C','7D','7E' ]


def main():
  parser = argparse.ArgumentParser()
  parser.add_argument('-s', '--start', action='store', dest='start_address', help='Starting Hex Address')
  parser.add_argument('-e', '--end', action='store', dest='end_address', help='Ending Hex Address')
  args = parser.parse_args()

  args.start_address = "0x08048000"
  args.end_address = "0X0804b000"
  s_addy = int(args.start_address,16)
  e_addy = int(args.end_address,16)
  
  #print "%s" % s_addy
  #print "%s" % e_addy


  while (s_addy <= e_addy):
       legit_addy = True
       s_addy = s_addy + 1
       h_str = hex(s_addy)
       if not h_str[2:4] in alphanum:
           legit_addy = False
       if not h_str[4:6] in alphanum:
           legit_addy = False
       if not h_str[6:8] in alphanum:
           legit_addy = False
       if not h_str[8:10] in alphanum:
           legit_addy = False
       if legit_addy == True:
            print "%s : Found" % (h_str)
       #else:
       #     print "%s : Bad" % (h_str)
       
if __name__ == '__main__':
  main()



