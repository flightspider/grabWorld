#coding=utf-8
# author:flightspider
# under MIT License
import re
import os
import urllib
import urlparse

path=raw_input("Please input the homepage:\n")
s='h'
ftype=raw_input('What\'s  type?\n')
ustc_staff="http://staff.ustc.edu.cn/"
if path.find(ustc_staff)== 0:
    root_dir = path[len(ustc_staff):]
else:
    root_dir = path[7:]
root_dir = root_dir.replace('.','_')
root_dir = root_dir.replace('/','-')
root_dir = root_dir+'/'
print 'root_dir:'+root_dir
#path='http://staff.ustc.edu.cn/~phj/mechanics/mechanics.htm'
#ftype='pdf'
def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

def getImg(html):
    reg =r'href="([^"]+\.'+ftype+')">'
    #http://vbird.dic.ksu.edu.tw/linux_server/0105beforeserver_3.php
    print reg
    imgre = re.compile(reg)
    imglist = re.findall(imgre,html)
    x = 0
    print  imglist
    l=len(imglist)
    for imgurl in imglist:
       print '> '+str(x)+'  /  '+str(l)+'\t..........'+imgurl
       imgpath=root_dir + os.path.split(imgurl)[0]       
       if imgpath!='':
            if not os.path.exists(imgpath):
              os.mkdir(imgpath)
       urllib.urlretrieve(urlparse.urljoin(path,imgurl),imgpath+imgurl)
       print urlparse.urljoin(path,imgurl)
       x=x+1
    return '$'+str(x)+'\t files fetched from '+str(l)+'\t found'     
   
html = getHtml(path)
#print html
print getImg(html)
