import re

from . import errors


def is_integer(num):
    #проверка на положительные и отрицательные целые числа в str
    if num[0]=='-':
        return num[1:].isdigit()
    else:return num.isdigit()
def is_real(num):
    #проверка на вещественные числа
    if '.' in num:
        num=num.split('.')
        return is_integer(num[0])and num[1].isdigit
        #часть до точки может иметь минус, часть после нет
    return is_integer(num)

def is_operator(char):
    return char in['+','-','/','*']
    #проверка на операторы

def bin_operation(a,b,operator):
    if operator=='+':
        return float(a)+float(b)
    if operator=='-':
        return float(a)-float(b)
    if operator=='*':
        return float(a)*float(b)
    if operator=='/':
        if float(b)==float(0):
            #ловим ошибку деления на ноль
            errors.expression_error(0)
            return False
        return float(a)/float(b)
def string_token(string):
    if errors.string_error(string): return '--'
    #ловим потенциальные ошибки, способные сломать дальнейшие преобразования
    string=string.replace(' ','')
    #игнорируем пробелы
    result=re.split(r'(\D)',string)
    #делим на числа и знаки
    while '' in result:
        result.remove('')
        #удаляем образовавшиеся пустые строки
    if errors.result_error(result):return'--'
    #ловим потенциальные ошибки
    if result[0]=='-' and result[1].isdigit:
        result=([result[0]+result[1]]+result[2:])
    #собираем отрицательное число в начале (если есть)
    
    while True:
        stop=1
        for i in range(len(result)):
            if result[i]=='-' and result[i+1].isdigit and not is_operator(result[i + 1]) and is_operator(result[i - 1]):
                result=(result[:i]+[result[i]+result[i+1]]+result[i+2:])
                stop=0
                break
        if stop==1:break
    #собираем отрицательные числа пока находим тройку оператор-минус-число
    if result[0]=='+' and result[1].isdigit and not is_operator(result[1]) and not is_operator(result[1]):
        result=result[1:]
    #убираем унарный плюс в начале (если есть)
    while True:
        stop=1
        for i in range(len(result)):
            if result[i]=='+' and result[i+1].isdigit and not is_operator(result[i + 1]) and is_operator(result[i - 1]):
                result=(result[:i]+result[i+1:])
                stop=0
                break
        if stop==1:break
        #убираем унарные плюсы пока находим тройку оператор-плюс-число
    while True:
        stop=1
        for i in range(1,len(result)-1):
            if is_integer(result[i - 1]) and result[i]== '.' and result[1 + i].isdigit():
                result=(result[:i-1]+[result[i-1]+'.'+result[i+1]]+result[i+2:])
                stop=0
                break
        if stop==1:break
    return result
    #собираем числа с точкой пока находим тройку целое число-точка-,беззнак_число
def valid(st):
    #валидация результата string_token
    if '--' in st or '-+'in st:return False
    #ищет слипшиеся унарные знаки
    for i in st:
        if not (is_real(i) or is_operator(i)):
            return False
        #проверяет на соответствие числу или оператору
    for i in range(1,len(st),2):
        if i==len(st)-1:return False
        if not is_operator(st[i]) or is_operator(st[1 + i]) or is_operator(st[i - 1]):
            return False
        #идет по ячейкам, которые должны указывать на операцию и находится между числами
    return True

def reverse_polish_notation(exp):
    #revers_polish_notation - обратная польская запись
    rpn_list=[]
    box=[] #доп стек для хранения неприоритетного оператора
    skip=0
    for i in range(len(exp)):

        if skip==1:
            skip=0
            continue
        #если предыдущая итерация приняла оператор => этот операнд уже добавлен

        if not is_operator(exp[i]):rpn_list.append(exp[i])
        else:
            rpn_list.append(exp[i+1])
            #вытаскиваем второй операнд к первому (1+2*3=>1 2 ...=>1 2 3 * +)
            if exp[i] in ['*','/']:
                rpn_list.append(exp[i])
                #приоритетный оператор можно добавить сразу
                if box:
                    #если box содержит непри-й оператор смотрим, можно ли его добавить
                    if i==len(exp)-2:rpn_list.append(box.pop())
                    #если ячейка последнего опертора, дальше точно нет оперторов
                    else:
                        if exp[i+2] not in ['*','/']:rpn_list.append(box.pop())
                        #проверяем ячейку следущего оператора,
                        #если он неприор-й вытаскиваем из box непр-й оператор
            if exp[i] in ['+','-']:
                if i==len(exp)-2:rpn_list.append(exp[i])
                #если мы в ячейке последнего оператора приор-сть уже не важна
                elif exp[i+2] in ['*','/']:box.append(exp[i])
                #если след оператор приор-й берем текущ в box,
                #чтоб перенести через прир-й(е) оператор(ы)
                else:rpn_list.append(exp[i])
            skip=1
    return rpn_list
        

def calc(expression):
    if not valid(string_token(expression)):
        errors.expression_error()
        return False
    #валидируем массив токенов перед тем как форматировать его в rpn
    expression=reverse_polish_notation(string_token(expression))
    stack=[]
    #создаем стек для вычисления
    for element in expression:
        if not is_operator(element):stack.append(element)
        #добавляем в стек операнды пока не дойдем до оператора
        else:
            #если дошли до оператора, берем последние два операнда и осущ арифм операцию
            num_b=stack.pop()
            num_a=stack.pop()
            stack.append(bin_operation(num_a,num_b,element))
            #возвращаем результат бин опер в стек

    return stack[0] #в стеке должен остаться только одно значение - результат
        


