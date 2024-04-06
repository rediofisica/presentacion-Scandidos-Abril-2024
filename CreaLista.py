#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 11 08:16:45 2022

@author: manuel
"""
import re
import sys
import os

print("Uso: Crealista.py HTMLFILE\n")
print("Convierte el fichero HTMLFILE y descarga las imágenes \n")

# pass the filename from the arguments
filename=sys.argv[1]

# Find all image links and generate a list to download with wget
f = open(filename, "rt")
text=f.read()
x = re.findall("https://s3.amazonaws.com/media-p.slid.es/uploads/111310/images/.*?\"", text)
y = re.findall("https://s3.amazonaws.com/media-p.slid.es/videos/111310/.*?\"", text)
w=open("wget.txt", "wt")
for item in x:
        # write each item on a new line
        w.write("%s\n" % item[:-1])
w.close()
w=open("wget2.txt", "wt")
for item in y:
        # write each item on a new line
        w.write("%s\n" % item[:-1])
w.close()



# Replacement of image links with local references and write to new html file "new.html"
text2=re.sub("https://s3.amazonaws.com/media-p.slid.es/uploads/111310/images/", "./images/", text)
text3=re.sub("https://s3.amazonaws.com/media-p.slid.es/videos/111310/", "./111310/", text2)
f2=open("new.html", "wt")
f2.write(text3)

f.close()
f2.close()

#Download the list of files in wget.txt using wget from bash shell
os.system("wget -i wget.txt -r -np -nH --cut-dirs=3")
#-i wget.txt descarga la lista de archivos en wget.txt
# -r : recursively
# -np : not going to upper directories, like ccc/…
# -nH : not saving files to hostname folder
# --cut-dirs=3 : but saving it to ddd by omitting first 3 folders aaa, bbb, ccc

os.system("wget -i wget2.txt -r -np -nH --cut-dirs=2")


