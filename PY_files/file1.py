################################## FILE HANDLINGS ##################################################
"""These are 5 properties of files @ name,mode,readable,writable,closed"""
f=open("abc.txt",'r+')
print("File Name: ",f.name)
print("File Mode: ",f.mode)
print("Is File Readable: ",f.readable())
print("Is File Writable: ",f.writable())
print("Is File Closed : ",f.closed)
f.close()
print("Is File Closed : ",f.closed)

########################### write & writelines ############################
print("-------write----->\n")
f=open("abcde.txt",'w+')  #to write
f.write("krishna\n")
f.write("Software\n")
f.write("Solutions\n")
print("Data written to the file successfully")
#f.close()
#f=open("abcd.txt",'r')  #to read
pos1=f.tell()
print("current position of fptr after writing",pos1)
pos2=f.seek(0,0)
print(" position of fptr to read",pos2)
rd=f.read()
print(rd)
f.close()
############################################
print()
f=open("abcde.txt",'w')
list=["hari\n","teja\n","hema\n","mounika"]
rd=f.writelines(list)   #to write no.of lines at time
print(rd)
f.close()
print("List of lines written to the file successfully")

################### read, read(n), readline() readlines() ###################
print("read----->\n")
f=open("abcd.txt","r")
a=f.read()  #prints whole data
print(a,"\n**********************************************\n")
p=f.seek(0,0)
a=f.read(10)        #prints 'n' chars
print(a,"\n**********************************************\n")
p=f.seek(0,0)
a=f.readline()  #prints first line if no arguments and also can read 'n' characters by arguments
b=f.readline()  #prints second line
c=f.readline(3)  #by giving int in readline it prints upto that no.of chars and it treats remaining chars as a next line
print(a,"\n***************************************************\n")
print(b)
print(c)
p=f.seek(0,0)
a=f.readlines()    # """all lines comes in list format only
                    #if arguments are zero or empty
                    # else prints first line in list format""
print(a,"\n***************************************************\n")
print("end of program")      
