lenUn=['mm','cm','m','km']
masUn=['g','kg']
temUn=['c','f','k']
def er(n):
    if n==0:print('incorect unit')
    if n==1:print('diffrent units')
    if n==2:print('lower abs zero')
def whUn(un):
    if un in lenUn:return 1
    if un in masUn:return 2
    if un in temUn:return 3
    return 0
def corUn(a,b):
    if whUn(a)*whUn(b)==0:
        er(0)
        return False
    if whUn(a)==whUn(b):return True
    er(1)
    return False

def main(n,unA,unB):
    unA=unA.lower()
    unB=unB.lower()
    if corUn(unA,unB):
        if unA=='kg':
            if unB=='g':return float(n)*1000
            if unB=='kg':return  float(n)
        if unA=='g':
            if unB=='g':return float(n)
            if unB=='kg':return  float(n)/1000
        if unA=='km':
            if unB=='mm':return float(n)*1000000
            if unB=='cm':return  float(n)*100000
            if unB=='m':return float(n)*1000
            if unB=='km':return  float(n)
        if unA == 'm':
            if unB == 'km': return float(n) / 1000
            if unB == 'mm': return float(n) * 1000
            if unB == 'cm': return float(n) * 100
            if unB == 'm': return float(n)
        if unA == 'cm':
            if unB == 'km': return float(n) / 100000
            if unB == 'm': return float(n) / 1000
            if unB == 'mm': return float(n) * 10
            if unB == 'cm': return float(n)
        if unA == 'mm':
            if unB == 'km': return float(n) / 1000000
            if unB == 'm': return float(n) / 1000
            if unB == 'cm': return float(n) / 10
            if unB == 'mm': return float(n)


        if unA=='c':
            if float(n)<-273.15:
                er(2)
                return False
            if unB=='c':return float(n)
            if unB=='f':return  (float(n)*1.8)+32
            if unB == 'k': return float(n)+273.15
        if unA == 'f':
            if float(n)<-459.67:
                er(2)
                return False
            if unB == 'c': return (float(n)-32)*5/9
            if unB == 'f': return float(n)
            if unB == 'k': return (float(n)+459.67)*5/9
        if unA=='k':
            if unA[0]=='-':
                er(2)
                return False
            if unB=='c':return float(n)-273.15
            if unB=='f':return  32+(float(n)-273.15)*1.8
            if unB == 'k': return float(n)

    return False
while True:
    ex=input().split()
    if ex[0]=='stop':break
    print(main(ex[0],ex[1],ex[2]))