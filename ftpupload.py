#!/usr/bin/env python3
#
# Script om files te uploaden naar webhost

import os
import sys
import ftplib 

if len(sys.argv) >  1: upfile = sys.argv[1]

updir1 = 'ftp host file directory 1' 
updir2 = 'ftp host file directory 2' 

if sys.argv[2] == 'uitlaat':
    updir = updir1
if sys.argv[2] == 'brief':
    updir = updir2

localfile = open(upfile, 'rb') 

ftp = ftplib.FTP('ftp.hostname.suffix')
ftp.login('ftp login name',passwd='')
ftp.cwd(updir) 
ftp.storbinary( 'STOR ' + upfile, localfile, 1024 )
ftp.quit()
localfile.close() 
