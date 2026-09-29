import re
import sys

from . import calc


def string_error(string):
    #проверяем на пропущенный опертор (пример: 67 + 42 52 * -22.8)
    #чтобы не получит 4252 после преобразования
    if re.search(r"\d\s\d",string):
        expression_error(2)
        return True
    #проверяем на непустую строку (считаем строку из одних пробелов пустой)
    string=string.replace(' ','')
    if string=='':
        expression_error(1)
        return True
    return False
def result_error(result):
    # проверяем на три оператора подряд (чтоб не "слиплись" унарные знаки)
    for i in range(1,len(result)-1):
        if calc.is_operator(result[i - 1])and calc.is_operator(result[i]) and calc.is_operator(result[i + 1]):
            expression_error()
            return True
    #проверяем на остутсвие последнего операнда, чтоб не выйти за пределы выражения
    if calc.is_operator(result[-1]):
        expression_error()
        return True
    if result[-1]=='.':
        expression_error()
        return True
    if result[0]=='.':
        expression_error()
        return True
    #проверяем на наличие элемента справа и слева от точки, чтоб не выйти за пределы выражения
    for i in range(1,len(result)-2):
        if result[i]=='.'and result[1+i]=='.' or result[i]=='.'and result[1+i]=='+':
            #проверяем на '..', '.+'
            expression_error()
            return True
def expression_error(n=None):
    #выводим в stderr ошибки калькулятора и завершаем с кодом ошибки 2
    if n==None:sys.stderr.write( 'invalid syntaxis')
    if n==1:sys.stderr.write( 'empty string')
    if n==2:sys.stderr.write( 'skipped operator')
    if n==0:sys.stderr.write( 'zero division error')
    sys.exit(2)
    
def convert_errors(n):
    #выводим в stderr ошибки конвертера и завершаем с кодом ошибки 2
    if n==0:sys.stderr.write('incorrect unit')
    if n==1:sys.stderr.write('different units')
    if n==2:sys.stderr.write('lower abs zero')
    if n==3:sys.stderr.write('incorrect input')
    sys.exit(2)


