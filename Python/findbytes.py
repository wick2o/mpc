#!/usr/bin/python

import struct
import sys

global quitme
quitme = 0
global mybit_results
mybit_results = [ [ 0 for i in range(4) ] for j in range(4) ]
global mybit_counter
mybit_counter = 0
tweaker = 0
need_tweak = 0

#print "input: " + sys.argv[1]

my_input = sys.argv[1][6:8] + sys.argv[1][4:6] + sys.argv[1][2:4] + sys.argv[1][0:2]
my_output = sys.argv[2]

myhex = int("FFFFFFFF",16) - int(str(my_input),16) + 1
myhex_string = hex(myhex)

#print my_input
#print myhex_string
#print str(len(myhex_string))

if str(len(myhex_string)) == "10":
    myhex_string = hex(int("0" + myhex_string[2:][0:7],16))
    #print "I come from 10: " + myhex_string
elif str(len(myhex_string)) == "9":
    myhex_string = "0x00" + myhex_string[2:8]
    #print "I come from 9: " + myhex_string

myhex_bits = [myhex_string[2:4],myhex_string[4:6],myhex_string[6:8],myhex_string[8:10]]
#print "myhex_bits: " + myhex_string[2:4] + " " + myhex_string[4:6] + " " + myhex_string[6:8] + " " + myhex_string[8:10]

bits=['01','02','03','04','05','06','07','08','0B','0C','0E','0F',
      '10','11','12','13','14','15','16','17','18','19','1A','1B',
      '1C','1D','1E','1F','14','15','16','17','18','19','1A','1B',
      '1C','1D','1E','1F','7F','30','31','32','33','34','35','36',
      '37','38','39','3B','3C','3D','3E','41','42','43','44','45',
      '46','47','48','49','4A','4B','4C','4D','4E','4F','50','51',
      '52','53','54','55','56','57','58','59','5A','5B','5D','5E',
      '5F','60','61','62','63','64','65','66','67','68','69','6A',
      '6B','6C','6D','6E','6F','70','71','72','73','74','75','76',
      '77','78','79','7A','7B','7C','7D','7E','7F']

for mybit in myhex_bits:
    #print mybit + "." * (mybit_counter + 1)
    if quitme == 1:
        quitme = 0
    for bit_01 in bits:
        if quitme == 1:
            break
        for bit_02 in bits:
            if quitme == 1:
                break
            for bit_03 in bits:
                mytotal = int(bit_01,16) + int(bit_02,16) + int(bit_03,16)
                if int(mybit,16) == mytotal:
                    mybit_results[mybit_counter] = [bit_01,bit_02,bit_03]
                    mybit_counter = mybit_counter + 1
                    quitme = 1
                    break
                else:
                    if len(hex(mytotal)) == 5:
                        if mybit == hex(mytotal)[3:5]:
                            mybit_results[mybit_counter] = [bit_01,bit_02,bit_03]
                            mybit_counter = mybit_counter + 1
                            quitme = 1
                            break

for i in range(0,4):
    if int(mybit_results[i][0],16) + int(mybit_results[i][1],16) + int(mybit_results[i][2],16) == 256:
        if i == 0:
            #tweaker += int("100000000",16)
             tweaker = 0
        elif i == 1:
            tweaker += int("1000000",16)
        elif i == 2:
            tweaker += int("10000",16)
        elif i == 3:
            tweaker += int("100",16)


#print hex(int(str(mybit_results[0][0]) + str(mybit_results[1][0]) + str(mybit_results[2][0]) + str(mybit_results[3][0]),16))

#print "Tweaker: " + hex(tweaker)


af_tweaker = hex(int(str(mybit_results[0][0]) + str(mybit_results[1][0]) + str(mybit_results[2][0]) + str(mybit_results[3][0]),16) + int(str(mybit_results[0][1]) + str(mybit_results[1][1]) + str(mybit_results[2][1]) + str(mybit_results[3][1]),16) + int(str(mybit_results[0][2]) + str(mybit_results[1][2]) + str(mybit_results[2][2]) + str(mybit_results[3][2]),16) - tweaker)


#print mybit_results

#print "After tweaker: " + af_tweaker

#print mybit_results

if my_output == "A":
    print "and eax,554E4D4A"
    print "and eax,2A313235"
    print "sub eax," + str(mybit_results[0][0]) + str(mybit_results[1][0]) + str(mybit_results[2][0]) + str(mybit_results[3][0])
    print "sub eax," + str(mybit_results[0][1]) + str(mybit_results[1][1]) + str(mybit_results[2][1]) + str(mybit_results[3][1])
    eax = hex(int(str(mybit_results[0][2]) + str(mybit_results[1][2]) + str(mybit_results[2][2]) + str(mybit_results[3][2]),16) - tweaker)[2:]
    print "sub eax," + eax
    print "push eax"
elif my_output == "C":
    print "\\x25\\x4A\\x4D\\x4E\\x55\\x25\\x35\\x32\\x21\\x2A" + "\\x2D\\x" + str(mybit_results[3][0]) + "\\x" + str(mybit_results[2][0]) + "\\x" + str(mybit_results[1][0]) + "\\x" + str(mybit_results[0][0]) + "\\x2D\\x" + str(mybit_results[3][1]) + "\\x" + str(mybit_results[2][1]) + "\\x" + str(mybit_results[1][1]) + "\\x" + str(mybit_results[0][1]) + "\\x2D\\x" + str(mybit_results[3][2]) + "\\x" + str(mybit_results[2][2]) + "\\x" + str(mybit_results[1][2]) + "\\x" + str(mybit_results[0][2])

                
