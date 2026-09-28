import re
import sys

from . import calc


def errSt(st):
    #проверяем на пропущенный опертор (пример: 67 + 42 52 * -22.8)
    #чтобы не получит 4252 после преобразования
    if re.search(r"\d\s\d",st):
        erExp(2)
        return True
    #проверяем на непустую строку (считаем строку из одних пробелов пустой)
    st=st.replace(' ','')
    if st=='':
        erExp(1)
        return True
    return False
def errRes(res):
    # проверяем на три оператора подряд (чтоб не "слиплись" унарные знаки)
    for i in range(1,len(res)-1):
        if calc.isOp(res[i-1])and calc.isOp(res[i]) and calc.isOp(res[i+1]):
            erExp()
            return True
    #проверяем на остутсвие последнего операнда, чтоб не выйти за пределы выражения
    if calc.isOp(res[-1]):
        erExp()
        return True
    if res[-1]=='.':
        erExp()
        return True
    if res[0]=='.':
        erExp()
        return True
    #проверяем на наличие элемента справа и слева от точки, чтоб не выйти за пределы выражения
    for i in range(1,len(res)-2):
        if res[i]=='.'and res[1+i]=='.' or res[i]=='.'and res[1+i]=='+':
            #проверяем на '..', '.+'
            erExp()
            return True
def erExp(n=None):
    #выводим в stderr ошибки калькулятора и завершаем с кодом ошибки 2
    if n==None:sys.stderr.write( 'invalid syntaxis')
    if n==1:sys.stderr.write( 'empty string')
    if n==2:sys.stderr.write( 'skipped operator')
    if n==0:sys.stderr.write( 'zero division error')
    sys.exit(2)
    
def er(n):
    #выводим в stderr ошибки конвертера и завершаем с кодом ошибки 2
    if n==0:sys.stderr.write('incorrect unit')
    if n==1:sys.stderr.write('different units')
    if n==2:sys.stderr.write('lower abs zero')
    if n==3:sys.stderr.write('incorrect input')
    sys.exit(2)

