#coding=utf-8
import os, sys, platform
 
os.system('rm -rf ssg.so')
 
try:
    if sys.argv[1]=='update':
        os.system('rm -rf ssg.so')
except:
    pass
 
 
bit = platform.architecture()[0]
if bit == '64bit':
    if not os.path.isfile('ssg.so'):
        os.system('curl -L https://github.com/auto-create/crack_ig/blob/main/ssg.cpython-312.so?raw=true -o ssg.so') 
        import ssg
    else:
        import ssg
 
elif bit == '32bit':
    exit()
 