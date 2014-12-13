from urllib import *
from os import *
import lxml.html

out="C:\\Music\\"; links=[]

# I used to download embedded MP3 soundtracks with this...

def urls(link):
    a=set(); dom=lxml.html.fromstring(urlopen(link).read())
    for l in dom.xpath('//a/@href'):
        if '#' not in l and 'mp3' in l: a.update([l])
    return list(a)

def get():
    for link in links:
        k=link.split('/')[-1]
        try: mkdir(out+k)
        except WindowsError: print "\n[FOLDER] %s already exists!\n"%k
        for i in urls(link):
            l=urls(i)[0]; m=l.split('/')[-1]
            if m in listdir(out+k):
                print "[File] %s already exists!"%m      # path.getsize() can also be used
                if stat(out+k+'\\'+m).st_size==int(urlopen(l).info()['Content-Length']): continue
                else:
                    s=str(raw_input("\tFile has different size! Overwrite (y/n)? "))
                    if s=='y': print "Downloading",l,"..."; urlretrieve(l,out+k+'\\'+m); continue
                    else: print "File skipped!"; continue
            print "Downloading",l,"..."; urlretrieve(l,out+k+'\\'+m)
