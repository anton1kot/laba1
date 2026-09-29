import sys

from . import calc, convert


def main():
    args=sys.argv[1:]
    #убираем из рассмотрения "toolkit"
    comm=args[0]
    #смотрим, что выполнить: calc convert --help
    if comm=='--help':
        sys.stdout.write('''
Usage:
    python -m toolkit calc EXPRESSION
        Принимает целые и вещественные числа, поддерживает унарный + или -
        Доступные операторы: + - / *
        Игнорирует пробелы между числами и операторами
            calc 2 + 3 * 4  # Вернёт 14.0
            calc +2*-4  # Вернёт -0.5
            calc 123 + 3 4  # Выведет ошибку "skipped operator"
            
    python -m toolkit convert VALUE --from UNIT --to UNIT
        Прнимает целые и вещественные числа
        Допустимые единицы измерения:
            Масса: kg g
            Расстояние: km m cm mm
            Температура: C F K
        Регистр не имеет значения
        Температура ниже абсолютного нуля выведет ошибку
            convert 0.001 --from kg --to g    # Вернёт 1.0
            convert 4 --from Mm --to MM    # Вернёт 4.0
            convert -459.67052 --from F to K   # Выведет ошибку "lower abs zero"    
        ''')
    argu = ' '.join(args[1:])
    #собираем аргументы
    if comm=='calc':
        sys.stdout.write(str(calc.calc(argu)))
    if comm=='convert':
        sys.stdout.write(str(convert.convert(argu)))
    #выводим результат

if __name__=="__main__":
    main()