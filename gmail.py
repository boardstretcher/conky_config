# This script isn't mine. I found it on a forum with no license
# and no authorship. Rights are the original author's.


import sys
import urllib             # For BasicHTTPAuthentication
import feedparser         # For parsing the feed
from textwrap import wrap

_URL = "https://mail.google.com/gmail/feed/atom"

uname = "YOUREMAIL@GMAIL.COM" 
password = "SOMEPASSWORD"
maxlen = 46

urllib.FancyURLopener.prompt_user_passwd = lambda self, host, realm: (uname, password)
	
def auth():
    '''The method to do HTTPBasicAuthentication'''
    opener = urllib.FancyURLopener()
    f = opener.open(_URL)
    feed = f.read()
    return feed


def readmail(feed, maxlen):
	'''Parse the Atom feed and print a summary'''
	atom = feedparser.parse(feed)
	print '%s new email(s)' % (len(atom.entries))
	#for i in range(min(len(atom.entries), maxlen)):
		#print '%s' %atom.entries[i].author
		#print '%s' %atom.entries[i].title

	#if len(atom.entries) > maxlen:
		#print '\n          more...'

if __name__ == "__main__":
    f = auth()  # Do auth and then get the feed
    readmail(f, int(maxlen)) # Let the feed be chewed by feedparser
