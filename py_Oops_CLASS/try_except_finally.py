############### Exception Handlings ##########################
##import os
##
##try:
##    x=int(input("enter num"))
##    y=int(input("enter sec num"))
##    print(x//y)
##    os._exit(0)
##except ZeroDivisionError:
##    print("zero division error\n")
##except ValueError:
##    print("enter integer value")
##finally:
##    print("finnally works")
                
####################### logging #############################
##
##import logging
##logging.basicConfig(filename="hk.txt",level=logging.DEBUG)
##logging.info(" -------A new request came----")
##try:
##    x=int(input("enter number------"))
##    y=int(input("enter sec number------"))
##    print(x/y)
##except ZeroDivisionError:
##    print("cannot divide with zero------")
##    logging.exception("------zero---")
##except ValueError :
##    print("enter only int value")
##    logging.exception("---logging---")
##logging.info("----------request processing completed--------")

##################### Assertions #######################
def squr(x):
    return x*x
assert squr(2)==4
assert squr(3)==16
assert squr(6)==36
print("2 srt is",squr(2))
print("4 srt",squr(4))
print("6 squr",squr(6))

    
    
