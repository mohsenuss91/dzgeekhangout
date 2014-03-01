#!/usr/bin/python2

import re, urllib2, json

print "Dont mind me :3  Jsut trying somehting :P"
print re.findall('[0,1]+',json.load(urllib2.urlopen('https ://api.duckduckgo. com/?q=I\'m+just+trying+something+to+binary&format=json'.replace(" ","")))["Answer"])[0]
