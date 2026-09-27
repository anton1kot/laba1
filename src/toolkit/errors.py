import re
import sys
from . import calc
def errSt(st):
    if re.search(r"\d\s\d",st):
        print(9)
        erExp(2)
        return True
    if st=='':
        erExp(1)
        return True
    return False
def errRes(res):
    for i in range(1,len(res)-1):
        if calc.isOp(res[i-1])and calc.isOp(res[i]) and calc.isOp(res[i+1]):
            erExp()
            return True
    if calc.isOp(res[-1]):
        erExp()
        return True
    if res[-1]=='.':
        erExp()
        return True
    if res[0]=='.':
        erExp()
        return True
    for i in range(1,len(res)-2):
        if res[i]=='.'and res[1+i]=='.':
            erExp()
            return True
def erExp(n=None):
    if n==None:sys.exit( 'invalid syntaxis')
    if n==1:sys.exit( 'empty string')
    if n==2:sys.exit( 'skipped operand')
    if n==0:sys.exit( 'zero division error')
def er(n):
    if n==0:sys.exit('incorrect unit')
    if n==1:sys.exit('different units')
    if n==2:sys.exit('lower abs zero')
    if n==3:sys.exit('incorrect input')

