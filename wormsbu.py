__author__ = 'Administrator'
# access the webpage of the internet
import urllib

import webbrowser
url = 'http://www.163.com'
content = urllib.urlopen(url).read()
open('163.com.html','w').write(content)
#print content

webbrowser.open_new_tab('163.com.html')
