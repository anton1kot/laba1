import sys
from . import calc
from . import convert


def main():
    args=sys.argv[1:]
    comm=args[0]

    argu=' '.join(args[1:])
    if comm=='--help':
        sys.stdout.write('''
Usage:
    python -m toolkit calc EXPRESSION
        Принимает целые и вещественные числа, поддерживает унарный + или -
        Доступные операторы: + - / *
        Игнорирует пробелы между числами и операторами
            calc 2 + 3 * 4  # Вернёт 14.0
            calc +2*-4  # Вернёт -0.5
            
    python -m toolkit conv VALUE --from UNIT --to UNIT
        Прнимает целые и вещественные числа
        Допустимые единицы измерения:
            Масса: kg g
            Расстояние: km m cm mm
            Температура: C F K
        Регистр не имеет значения
        Температура ниже абсолютного нуля выведет ошибку
            conv 0.001 --from kg --to g    # Вернёт 1.0
            conv 4 --from Mm --to MM    # Вернёт 4.0
            conv -459.67052 --from F to K   # Выведет ошибку "lower abs zero"    
        ''')
    if comm=='calc':
        sys.stdout.write(str(calc.calc(argu)))
    if comm=='conv':
        sys.stdout.write(str(convert.conv(argu)))
if __name__=="__main__":
    main()