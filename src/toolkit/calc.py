import re
from . import errors
def isZ(n):
    if n[0]=='-':
        return n[1:].isdigit()
    else:return n.isdigit()
def isR(n):
    if '.' in n:
        n=n.split('.')
        return isZ(n[0])and n[1].isdigit
    return isZ(n)

def isOp(x):
    return x in['+','-','/','*']

def arif(a,b,c):
    if c=='+':
        return float(a)+float(b)
    if c=='-':
        return float(a)-float(b)
    if c=='*':
        return float(a)*float(b)
    if c=='/':
        if float(b)==float(0):
            errors.erExp(0)
            return False
        return float(a)/float(b)
def tokStr(st):
    if errors.errSt(st): return '--'
    st=st.replace(' ','')
    if errors.errSt(st):return'--'
    #end of str
    res=re.split(r'(\D)',st)
    while '' in res:
        res.remove('')
    if errors.errRes(res):return'--'
    
    if res[0]=='-' and res[1].isdigit:
        res=([res[0]+res[1]]+res[2:])
    
    while True:
        stop=1
        for i in range(len(res)):
            if res[i]=='-' and res[i+1].isdigit and not isOp(res[i+1]) and isOp(res[i-1]):
                res=(res[:i]+[res[i]+res[i+1]]+res[i+2:])
                stop=0
                break
        if stop==1:break

    if res[0]=='+' and res[1].isdigit and not isOp(res[1]) and not isOp(res[1]):
        res=res[1:]
    
    while True:
        stop=1
        for i in range(len(res)):
            if res[i]=='+' and res[i+1].isdigit and  not isOp(res[i+1]) and isOp(res[i-1]):
                res=(res[:i]+res[i+1:])
                stop=0
                break
        if stop==1:break
    while True:
        stop=1
        for i in range(1,len(res)-1):
            if isZ(res[i-1]) and res[i]=='.' and res[1+i].isdigit():
                res=(res[:i-1]+[res[i-1]+'.'+res[i+1]]+res[i+2:])
                stop=0
                break
        if stop==1:break
    return res
def valid(st):
    if '--' in st or '-+'in st:return False
    for i in st:
        if not (isR(i) or isOp(i)):
            return False
    for i in range(1,len(st),2):
        if i==len(st)-1:return False
        if st[i] not in ['+','-','/','*'] or st[1+i] in ['+','-','/','*'] or st[i-1] in ['+','-','/','*']:
            return False
    return True

def rpn(exp):
    st=[]
    box=[]
    skip=0
    for i in range(len(exp)):
        if skip==1:
            skip=0
            continue
        if not isOp(exp[i]):st.append(exp[i])
        else:
            st.append(exp[i+1])
            if exp[i] in ['*','/']:
                st.append(exp[i])
                if box:
                    if i==len(exp)-2:st.append(box.pop())
                    else:
                        if exp[i+2] not in ['*','/']:st.append(box.pop())
            if exp[i] in ['+','-']:
                if i==len(exp)-2:
                    st.append(exp[i])
                elif exp[i+2] in ['*','/']:box.append(exp[i])
                else:st.append(exp[i])
            skip=1
    return st
        

def calc(exp):
    if not valid(tokStr(exp)):
        errors.erExp()
        return False
    exp=rpn(tokStr(exp))
    stack=[]
    for el in exp:
        if not isOp(el):stack.append(el)
        else:
            b=stack.pop()
            a=stack.pop()
            stack.append(arif(a,b,el))
            if el=='/' and float(b)==float(0):return False
    return stack[0]
        

