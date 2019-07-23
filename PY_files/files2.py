############################## FILE HANDINGS 2 TEXT files ####################################################################
"""with statement closes file automatically after completion of all operations"""
with open("abcd.txt","r") as f:    
    print(f.read())
    print(f.closed)
print(f.closed)
###############################################################    
print()
f=open("hk.txt","w+") #f is file object
f.write("early morning sun rises inthe east and sun sets in the west")
f.seek(0,0)
rd=f.read()
print(rd)
f.seek(0)
print(f.read(10))
print("cur pos",f.tell())
f.seek(17)  #py3 takes only default "zero" or can give direct num
print(f.read())
###############################################################
print()
import os,sys
check=os.path.isfile("abcd.txt")
print(check)
#sys.exit(0)     #exit will terminates remaining prgm
print("welcome to votary")
#######################################################################
""" To find no.of line, no.of words,no.of characters in a file """
print("****************************")
f=open("abcd.txt","r")
#rd=f.read()
lc=wc=cc=0
for hari in f:    
    lc=lc+1
    cc=cc+len(hari)
    w=hari.split()  #it takes words as in list_format
    wc=wc+len(w)
print("no.of lines",lc)
print("no.of words",wc)
print("no.of chars",cc)
