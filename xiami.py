#!/usr/bin/env python
from pyquery import PyQuery as pq
from lxml import etree
import urllib
import urllib2
import time
import sys
import os

artist_name = sys.argv[1]
artist_url_name = urllib.quote(artist_name.decode(sys.stdin.encoding).encode('utf-8'));
xiami_url = 'http://www.xiami.com/search?key=' + artist_url_name + '&pos=1'
print xiami_url
d = pq(url=xiami_url)
try:
    p = d("div.artistBlock_list div.artist_item100_block p.buddy a.artist100")
    artist_url = p.attr('href')
    print artist_url
    artist_url = 'http://www.xiami.com' + artist_url
    print artist_url
    d = pq(url=artist_url)    
    p = d("a#cover_lightbox")
    cover_url = p.attr('href').encode("utf-8","ingnore")
    print cover_url
except Exception, e:
    print e
    sys.exit()

print cover_url
req = urllib2.Request(url=cover_url)
f= urllib2.urlopen(req)

(filepath,filename)=os.path.split(cover_url)
cover_type = os.path.splitext(filename)[1]

fp = open(artist_name.decode(sys.stdin.encoding).encode(sys.stdin.encoding) + cover_type.lower(), 'wb')
cover_data = f.read()
fp.write(cover_data)
fp.close()
