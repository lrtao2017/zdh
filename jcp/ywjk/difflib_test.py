#coding=utf-8

'''
python wjcy.py 1.txt 2.txt > test.html

'''
import difflib
import sys

try:
    textfile1=sys.argv[1]
    textfile2=sys.argv[2]
except Exception,e:
    print "Error:" + str(e)
    print "Usage:python wjcy.py filename1 filename2"
    sys.exit()
    
def readfile(filename):
    try:
        with open (filename,'rb') as fileHandle:
            text = fileHandle.read().splitlines()
        return text
    except IOError as error:
        print ('Read file Error:' + str(error))
        sys.exit()
        
tex1_lines = readfile(textfile1)
tex2_lines = readfile(textfile2)

d = difflib.HtmlDiff()
print d.make_file(tex1_lines,tex2_lines)
    
            
        
    
