# ###########  How to use instance variable #################
class hari:
    a=35435                     #static variable
    def __init__(self):
        self.eno=100
        self.ename="krishna"    #1..instance var
        self.esal=1000
        print(self.ename)       #1(a)..init using self
    def ram(self):
        self.some="12313234"
        print(self.esal)        #1(b)..method using self
    #print(hari.esal)
        
e=hari()
e.ram()
e.kri="120"                 #1...instance var out of the class
print(e.kri)    
del e.kri               #to delete instance variable          
#print(e.kri)           #to know object deleted
print()
####################################################################################

class test:                                
    def __init__(self):
        self.a=10
        self.b=20
t1=test()
t1.a=123
t1.b=433
t2=test()
print(" t1=",t1.a,t1.b," t2=",t2.a,t2.b)
print()
################################  Static variable ##############################
class test():
    a=100
    def __init__(self):
        test.b=20
        self.b=200
        print("in constructor",test.b,self.b)
    def m1(self):               #instance method0
            test.c=300
            print(self.b,test.b)
    @classmethod
    def m2(raju):               #class method
            test.d=400
            print("in m2",test.d)
    @staticmethod
    def m3():                   #static method
        test.e="krishnam raju"
        print(test.e)
    
t1=test()
t1.m1()
print("read static var with Ref var ",t1.c)
#del t1.c we can't delete/modify static var using ref var only can read
t1.m2()
t1.m3()
print("out class",t1.d)         #static variable accessing
##################### local variable #######################
print()
"""local variable is nothing but temperory variable which can declare inside of any method in class"""
class test():
    def __init__(self):
        a=20
        b=34
        print(a,b)
    #def raju(self):
        #print(a,b) #we can't access local variable from other methods
t1=test()
#t1.raju()
