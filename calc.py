import re
def isZ(n):
    if n[0]=='-':
        return n[1:].isdigit()
    else:return n.isdigit()

def isOp(x):
    return x in['+','-','/','*']
def errSt(st):
    if re.search(r'\d \d',st):
        print(erExp(2))
        return True
    if st=='':
        print(erExp(1))
        return True
    return False
def errRes(res):
    for i in range(1,len(res)-1):
        if isOp(res[i-1])and isOp(res[i]) and isOp(res[i+1]):
            erExp()
            return True
    if res[-1]=='-':
        erExp()
        return True
    if res[-1]=='+':
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
    if n==None:return 'invalid syntaxis'
    if n==1:return 'empty string'
    if n==2:return 'skipped operand'
    if n==0:return 'error zero del'
def arif(a,b,c):
    if c=='+':
        return float(a)+float(b)
    if c=='-':
        return float(a)-float(b)
    if c=='*':
        return float(a)*float(b)
    if c=='/':
        if float(b)==float(0):
            print(erExp(0))
            return False
        return float(a)/float(b)
def tokStr(st):
    st=st.replace(' ','')
    if errSt(st):return'--'
    #end of str
    res=re.split(r'(\D)',st)
    while '' in res:
        res.remove('')
    if errRes(res):return'--'
    
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
    stack=[]
    for el in exp:
        if not isOp(el):stack.append(el)
        else:
            b=stack.pop()
            a=stack.pop()
            stack.append(arif(a,b,el))
            if el=='/' and float(b)==float(0):return False
    return stack[0]
        
            
while True:
    a=str(input())
    if a=='stop':break
    if valid(tokStr(a)):
        print(calc(rpn(tokStr(a))))
    else:
        print(tokStr(a),'f')
