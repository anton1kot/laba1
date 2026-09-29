from . import errors


def what_type_of_units(un):
    if un in ['mm','cm','m','km']:return 1
    if un in ['g','kg']:return 2
    if un in ['c','f','k']:return 3
    #задаем каждой группе код
    return 0
    #неизвестные единицы получат код 0
def units_correlation(a,b): #корелляция единиц
    if what_type_of_units(a)*what_type_of_units(b)==0:
        #если хотя бы одна един неизв - ошибка неизв един
        errors.convert_errors(0)
        return False
    if what_type_of_units(a)==what_type_of_units(b):return True
    #если код групп не совпал - ошибка разн един
    errors.convert_errors(1)
    return False

def convert(expression):
    expression = expression.split()
    if len(expression)!=5:
        errors.convert_errors(3)
        return False
    if expression[1]!= '--from' or expression[3]!= '--to':
        errors.convert_errors(3)
        return False
    #разделяем аргументы и проверяем на корректность ввода
    num=expression[0]
    un_a=expression[2].lower()
    un_b=expression[4].lower()
    if units_correlation(un_a,un_b):
        if un_a=='kg':
            if un_b=='g':return float(num)*1000
            if un_b=='kg':return  float(num)
        if un_a=='g':
            if un_b=='g':return float(num)
            if un_b=='kg':return  float(num)/1000
        if un_a=='km':
            if un_b=='mm':return float(num)*1000000
            if un_b=='cm':return  float(num)*100000
            if un_b=='m':return float(num)*1000
            if un_b=='km':return  float(num)
        if un_a == 'm':
            if un_b == 'km': return float(num) / 1000
            if un_b == 'mm': return float(num) * 1000
            if un_b == 'cm': return float(num) * 100
            if un_b == 'm': return float(num)
        if un_a == 'cm':
            if un_b == 'km': return float(num) / 100000
            if un_b == 'm': return float(num) / 1000
            if un_b == 'mm': return float(num) * 10
            if un_b == 'cm': return float(num)
        if un_a == 'mm':
            if un_b == 'km': return float(num) / 1000000
            if un_b == 'm': return float(num) / 1000
            if un_b == 'cm': return float(num) / 10
            if un_b == 'mm': return float(num)

        #перед конвертацией проверим каждое значение относительно абсолютного нуля
        if un_a=='c':
            if float(num)<-273.15:
                errors.convert_errors(2)
                return False
            if un_b=='c':return float(num)
            if un_b=='f':return  (float(num)*1.8)+32
            if un_b == 'k': return float(num)+273.15
        if un_a == 'f':
            if float(num)<-459.67:
                errors.convert_errors(2)
                return False
            if un_b == 'c': return (float(num)-32)*5/9
            if un_b == 'f': return float(num)
            if un_b == 'k': return (float(num)+459.67)*5/9
        if un_a=='k':
            if un_a[0]=='-':
                errors.convert_errors(2)
                return False
            if un_b=='c':return float(num)-273.15
            if un_b=='f':return  32+(float(num)-273.15)*1.8
            if un_b == 'k': return float(num)

    return None