#!/usr/bin/python

import urllib, urllib2
import sys
from BeautifulSoup import BeautifulSoup

def main():

    for i in range(100):
        url = urllib2.urlopen('http://www.amazon.com/s?ie=UTF8&rh=n:5&page=%s' % (i))
        html = url.read()
  
        soup = BeautifulSoup(html)
        url_list = []

        for tag in soup.findAll('a', href=True):
            if "/dp/" in tag['href']:
                if "http://" in tag['href']:
                    if not tag['href'] in url_list:
                        url_list.append(tag['href'])
                        print "testing : %s" % tag['href']
                        item_url = urllib2.urlopen(tag['href'])
                        item_html = item_url.read()

                        item_soup = BeautifulSoup(item_html)
                        for item_tag in item_soup.findAll('a', href=True):
                            if "request-kindle-edition" in item_tag['href']:
                                print "Found kindle url...Requesting Now..."
                                print "Opening http://www.amazon.com%s" % (item_tag['href'])
                                idk_opener = urllib2.build_opener()
                                idk_opener.addheaders = [('User-agent', 'Mozilla/5.0')]
                                idk_html = idk_opener.open("http://www.amazon.com%s" % (item_tag['href'])).read()
                                print idk_html
                                if "kindleRequestThank" in idk_html:
                                    print "Request Worked"

if __name__ == '__main__':
    main()