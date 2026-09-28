from . import errors

lenUn=['mm','cm','m','km']
masUn=['g','kg']
temUn=['c','f','k']

def whUn(un):
    if un in lenUn:return 1
    if un in masUn:return 2
    if un in temUn:return 3
    #задаем каждой группе код
    return 0
    #неизвестные единицы получат код 0
def corUn(a,b): #корелляция единиц
    if whUn(a)*whUn(b)==0:
        #если хотя бы одна един неизв - ошибка неизв един
        errors.er(0)
        return False
    if whUn(a)==whUn(b):return True
    #если код групп не совпал - ошибка разн един
    errors.er(1)
    return False

def conv(ex):
    ex = ex.split()
    if len(ex)!=5:
        errors.er(3)
        return False
    if ex[1]!='--from' or ex[3]!='--to':
        errors.er(3)
        return False
    #разделяем аргументы и проверяем на корректность ввода
    n=ex[0]
    unA=ex[2].lower()
    unB=ex[4].lower()
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

        #перед конвертацией проверим каждое значение относительно абсолютного нуля
        if unA=='c':
            if float(n)<-273.15:
                errors.er(2)
                return False
            if unB=='c':return float(n)
            if unB=='f':return  (float(n)*1.8)+32
            if unB == 'k': return float(n)+273.15
        if unA == 'f':
            if float(n)<-459.67:
                errors.er(2)
                return False
            if unB == 'c': return (float(n)-32)*5/9
            if unB == 'f': return float(n)
            if unB == 'k': return (float(n)+459.67)*5/9
        if unA=='k':
            if unA[0]=='-':
                errors.er(2)
                return False
            if unB=='c':return float(n)-273.15
            if unB=='f':return  32+(float(n)-273.15)*1.8
            if unB == 'k': return float(n)

