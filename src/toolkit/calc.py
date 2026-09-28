import re

from . import errors


def isZ(n):
    #проверка на положительные и отрицательные целые числа в str
    if n[0]=='-':
        return n[1:].isdigit()
    else:return n.isdigit()
def isR(n):
    #проверка на вещественные числа
    if '.' in n:
        n=n.split('.')
        return isZ(n[0])and n[1].isdigit
        #часть до точки может иметь минус, часть после нет
    return isZ(n)

def isOp(x):
    return x in['+','-','/','*']
    #проверка на операторы

def arif(a,b,c):
    if c=='+':
        return float(a)+float(b)
    if c=='-':
        return float(a)-float(b)
    if c=='*':
        return float(a)*float(b)
    if c=='/':
        if float(b)==float(0):
            #ловим ошибку деления на ноль
            errors.erExp(0)
            return False
        return float(a)/float(b)
def tokStr(st):
    if errors.errSt(st): return '--'
    #ловим потенциальные ошибки, способные сломать дальнейшие преобразования
    st=st.replace(' ','')
    #игнорируем пробелы
    res=re.split(r'(\D)',st)
    #делим на числа и знаки
    while '' in res:
        res.remove('')
        #удаляем образовавшиеся пустые строки
    if errors.errRes(res):return'--'
    #ловим потенциальные ошибки
    if res[0]=='-' and res[1].isdigit:
        res=([res[0]+res[1]]+res[2:])
    #собираем отрицательное число в начале (если есть)
    
    while True:
        stop=1
        for i in range(len(res)):
            if res[i]=='-' and res[i+1].isdigit and not isOp(res[i+1]) and isOp(res[i-1]):
                res=(res[:i]+[res[i]+res[i+1]]+res[i+2:])
                stop=0
                break
        if stop==1:break
    #собираем отрицательные числа пока находим тройку оператор-минус-число
    if res[0]=='+' and res[1].isdigit and not isOp(res[1]) and not isOp(res[1]):
        res=res[1:]
    #убираем унарный плюс в начале (если есть)
    while True:
        stop=1
        for i in range(len(res)):
            if res[i]=='+' and res[i+1].isdigit and not isOp(res[i+1]) and isOp(res[i-1]):
                res=(res[:i]+res[i+1:])
                stop=0
                break
        if stop==1:break
        #убираем унарные плюсы пока находим тройку оператор-плюс-число
    while True:
        stop=1
        for i in range(1,len(res)-1):
            if isZ(res[i-1]) and res[i]=='.' and res[1+i].isdigit():
                res=(res[:i-1]+[res[i-1]+'.'+res[i+1]]+res[i+2:])
                stop=0
                break
        if stop==1:break
    return res
    #собираем числа с точкой пока находим тройку целое число-точка-,беззнак_число
def valid(st):
    #валидация результата tokStr
    if '--' in st or '-+'in st:return False
    #ищет слипшиеся унарные знаки
    for i in st:
        if not (isR(i) or isOp(i)):
            return False
        #проверяет на соответствие числу или оператору
    for i in range(1,len(st),2):
        if i==len(st)-1:return False
        if not isOp(st[i]) or isOp(st[1+i]) or isOp(st[i-1]):
            return False
        #идет по ячейкам, которые должны указывать на операцию и находится между числами
    return True

def rpn(exp):
    #revers_polish_notation - обратная польская запись
    st=[]
    box=[] #доп стек для хранения неприоритетного оператора
    skip=0
    for i in range(len(exp)):

        if skip==1:
            skip=0
            continue
        #если предыдущая итерация приняла оператор => этот операнд уже добавлен

        if not isOp(exp[i]):st.append(exp[i])
        else:
            st.append(exp[i+1])
            #вытаскиваем второй операнд к первому (1+2*3=>1 2 ...=>1 2 3 * +)
            if exp[i] in ['*','/']:
                st.append(exp[i])
                #приоритетный оператор можно добавить сразу
                if box:
                    #если box содержит непри-й оператор смотрим, можно ли его добавить
                    if i==len(exp)-2:st.append(box.pop())
                    #если ячейка последнего опертора, дальше точно нет оперторов
                    else:
                        if exp[i+2] not in ['*','/']:st.append(box.pop())
                        #проверяем ячейку следущего оператора,
                        #если он неприор-й вытаскиваем из box непр-й оператор
            if exp[i] in ['+','-']:
                if i==len(exp)-2:st.append(exp[i])
                #если мы в ячейке последнего оператора приор-сть уже не важна
                elif exp[i+2] in ['*','/']:box.append(exp[i])
                #если след оператор приор-й берем текущ в box,
                #чтоб перенести через прир-й(е) оператор(ы)
                else:st.append(exp[i])
            skip=1
    return st
        

def calc(exp):
    if not valid(tokStr(exp)):
        errors.erExp()
        return False
    #валидируем массив токенов перед тем как форматировать его в rpn
    exp=rpn(tokStr(exp))
    stack=[]
    #создаем стек для вычисления
    for el in exp:
        if not isOp(el):stack.append(el)
        #добавляем в стек операнды пока не дойдем до оператора
        else:
            #если дошли до оператора, берем последние два операнда и осущ арифм операцию
            b=stack.pop()
            a=stack.pop()
            stack.append(arif(a,b,el))
            #возвращаем результат бин опер в стек

    return stack[0] #в стеке должен остаться только одно значение - результат
        

