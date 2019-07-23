############################## FILE HANDLING_BINARY FILES ######################
f=open("Penguins.jpg","rb")
f2=open("peng_bom7.jpg","wb")
f3=open("peng_bom8.jpg","wb")  
bytes1=f.read()
f2.write(bytes1)
f3.write(bytes1)
print("new image ---- is avaiable")
f.close()
f2.close()  # must to close file to copy image
f3.close()
######################## CSV format ##############################
    #"""CSV is a simple file format used to store tabular data,such as a spreadsheet or database.
    #Files in the CSV format can be imported to and exported from programs that store data in tables,
    #such as Microsoft Excel or OpenOffice Calc.
    #CSV stands for "comma-separated values"."""

import csv
with open("emp2.csv","w") as f:
    w=csv.writer(f)      # returns csv writer object
    w.writerow(["ENO ENAME ESAL EADDR"])  #write column is not there
    n=int(input("Enter Number of Employees:"))
    for i in range(n):
        eno=input("Enter Employee No:")
        ename=input("Enter Employee Name:")
        esal=input("Enter Employee Salary:")       
        eaddr=input("Enter Employee Address:")
        w.writerow([eno,ename,esal,eaddr])
print("Total Employees data written to csv file successfully")
################### read format ##############
 import csv
with open("emp2.csv","r") as f:
    r=csv.reader(f)
    data=list(r)
    print(data) #prints data in list format
    for line in data:
        #for word in line:
            print(line)

    print()
