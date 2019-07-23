##############################FILES_ZIP ####################################


# importing required modules 
from zipfile import ZipFile 

# specifying the zip file name 
file_name = "Python37-32.zip"

# opening the zip file in READ mode 
with ZipFile(file_name, 'r') as f: 
	# printing all the contents of the zip file 
	f.printdir() 

	# extracting all the files 
	print('Extracting all the files now...') 
	f.extractall() 
	print('Done!') 
######################## working directories ###############
print()
import os
f=os.walk('tcl')
print("files are-------",f)

