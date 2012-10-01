#!/usr/bin/python

#This script requires pdfscan.exe and pdfid.py

import argparse, sys, os, fnmatch
import subprocess,datetime

now = datetime.datetime.now()
oname = str(now.year) + "-" + str(now.month) + "-" + str(now.day) + "-" + str(now.hour) + "-" + str(now.minute) + "-" + str(now.second) + "-" + str(os.getenv('USERNAME')) + ".txt"

def do_work():
    if not os.path.isdir(args.output):
        print "Output Path does not exist!!!"
        exit()
    else:
        ofname = args.output.strip() + oname
        ofile = open(ofname, "w")

    if os.path.isdir(args.folder):
            for file in os.listdir(args.folder):
                if fnmatch.fnmatch(file, '*.pdf'):
                    cmd = 'pdfscan.exe ' + "\"" + args.folder.strip() + "\\" + file + "\""
                    fin,fout = os.popen4(cmd)
                    output = fout.read()
                    if output.strip() == 'Clean':
                        os.remove(args.folder.strip() + "\\" + file)
                    elif output.strip() == 'Medium risk' or output.strip() == 'High risk':
                        cmd = 'pdfid.py ' + "\"" + args.folder.strip() + "\\" + file + "\""
                        fin,fout = os.popen4(cmd)
                        ofile.write(fout.read())
            ofile.close()
            os.system('notepad.exe ' + args.output.strip() + oname)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog='PDFScanner',
        add_help=False,
        description='''This software is meant to scan one or more PDFs''',
        epilog='''more description text here'''
        )
    parser.add_argument('-f', '--folder', required='True', nargs='?', help='Folder to scan for PDFs')
    parser.add_argument('-o', '--output', required='True', nargs='?', help='Folder to save output')

    args = parser.parse_args()
    do_work()
