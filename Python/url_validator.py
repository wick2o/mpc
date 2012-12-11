#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import socket
import argparse

domains_suffix = [ '.ac',     '.ac.uk',  '.ad',     '.ae',   '.aero', '.af',     '.ag',   '.ai',     '.al',     '.am',
				   '.an',     '.ao',     '.aq',     '.ar',   '.arpa', '.as',     '.asia', '.at',     '.au',     '.aw',
				   '.ax',     '.az',     '.ba',     '.bb',   '.bd',   '.be',     '.bf',   '.bg',     '.bh',     '.bi',
				   '.bj',     '.bm',     '.bn',     '.bo',   '.br',   '.bs',     '.bt',   '.bv',     '.bw',     '.by',
				   '.ca',     '.cat',    '.cc',     '.cd',   '.cf',   '.cg',     '.ch',   '.ci',     '.ck',     '.cl',
				   '.cn',     '.co',     '.co.uk',  '.com',  '.coop', '.cr',     '.cs',   '.cu',     '.cv',     '.cx',
				   '.cy',     '.cz',     '.biz',    '.bz',   '.cm',   '.dd',     '.de',   '.dj',     '.dk',     '.dm',
				   '.do',     '.dz',     '.ec',     '.edu',  '.ee',   '.eg',     '.eh',   '.er',     '.es',     '.et',
				   '.eu',     '.fi',     '.firm',   '.fj',   '.fk',   '.fm',     '.fo',   '.fr',     '.fx',     '.ga',
				   '.gb',     '.gd',     '.ge',     '.gf',   '.gh',   '.gi',     '.gl',   '.gm',     '.gn',     '.gov',
				   '.gov.uk', '.gp',     '.gq',     '.gr',   '.gs',   '.gt',     '.gu',   '.gw',     '.gy',     '.hk',
				   '.hm',     '.hn',     '.hr',     '.ht',   '.hu',   '.id',     '.ie',   '.il',     '.in',     '.info',
				   '.int',    '.io',     '.iq',     '.ir',   '.is',   '.it',     '.je',   '.jm',     '.jo',     '.jobs',
				   '.jp',     '.ke',     '.kg',     '.kh',   '.ki',   '.km',     '.kn',   '.kp',     '.kr',     '.kw',
				   '.ky',     '.kz',     '.la',     '.lb',   '.lc',   '.li',     '.lk',   '.lr',     '.ls',     '.lt',
				   '.ltd.uk', '.lu',     '.lv',     '.ly',   '.ma',   '.mc',     '.md',   '.me',     '.me.uk',  '.mg',
				   '.mh',     '.mil',    '.mk',     '.ml',   '.mm',   '.mn',     '.mo',   '.mobi',   '.mod.uk', '.mp',
				   '.mq',     '.mr',     '.ms',     '.mt',   '.mu',   '.museum', '.mv',   '.mw',     '.mx',     '.my',
				   '.mz',     '.na',     '.name',   '.nato', '.nc',   '.ne',     '.net',  '.net.uk', '.nf',     '.ng',
				   '.nhs.uk', '.ni',     '.nl',     '.no',   '.nom',  '.np',     '.nr',   '.nt',     '.nu',     '.nz',
				   '.om',     '.org',    '.org.uk', '.pa',   '.pe',   '.pf',     '.pg',   '.ph',     '.pk',     '.pl',
				   '.plc.uk', '.pm',     '.pn',     '.pr',   '.pro',  '.ps',     '.pt',   '.pw',     '.py',     '.qa',
				   '.re',     '.ro',     '.ru',     '.rw',   '.sa',   '.sb',     '.sc',   '.sch.uk', '.sd',     '.se',
				   '.sg',     '.sh',     '.si',     '.sj',   '.sk',   '.sl',     '.sm',   '.sn',     '.so',     '.sr',
				   '.ss',     '.st',     '.store',  '.su',   '.sv',   '.sy',     '.sz',   '.tc',     '.td',     '.tel',
				   '.tf',     '.tg',     '.th',     '.tj',   '.tk',   '.tl',     '.tm',   '.tn',     '.to',     '.tp',
				   '.tr',     '.travel', '.tt',     '.tv',   '.tw',   '.tz',     '.ua',   '.ug',     '.uk',     '.um',
				   '.us',     '.uy',     '.va',     '.vc',   '.ve',   '.vg',     '.vi',   '.vn',     '.vu',     '.web',
				   '.wf',     '.ws',     '.xxx',    '.ye',   '.yt',   '.yu',     '.za',   '.zm',     '.zr',     '.zw',
				 ]
		
		
def setup():
	parser = argparse.ArgumentParser()
	parser.add_argument('-f', '--file', action='store', dest='file', required=True,  help='File with urls, one per line')

	global args
	args = parser.parse_args()
	
def main():
	setup()
	
	urls = []
	valid = []
	notvalid = []
	
	url_file = open(args.file,'r')
	url_read = url_file.readlines()
	url_read = [item.strip() for item in url_read]
	for url in url_read:
		if not url.startswith('#'): #ignore comments
			urls.append(url)
	url_file.close()
	
	for url in urls:
		AmIValid = False
		for tld in domains_suffix:
			if url.endswith(tld):
				AmIValid = True
				break
		if AmIValid == True:
			valid.append(url)
		else:
			notvalid.append(url)
		
		
	v_urls = open('out_urls_valid.txt', 'wb')
	v_urls.write('\n'.join(valid))
	v_urls.close()
	
	nv_urls = open('out_urls_notvalid.txt', 'wb')
	nv_urls.write('\n'.join(notvalid))
	nv_urls.close()
	
	print 'completed'
	sys.exit()



if __name__ == "__main__":
	main()