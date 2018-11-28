#!/usr/bin/env python3
# _*_ coding: utf-8 -*
import urllib.request   # python 3.7
 
for i in range(150,500):
	url = 'http://placekitten.com/' + str(i) + '/200'
	response = urllib.request.urlopen(url)
	cat_img = response.read()
	name = '/Users/guokai/Desktop/cat/' + str(i) + '.jpg'
	with open (name,'wb') as f:
		f.write(cat_img)
		print ('下载完成第%d张猫片' % (i - 149))
 
 
 
 
 
