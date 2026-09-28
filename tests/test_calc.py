import pytest

from toolkit import calc


def test_simple_add():
    #проверка простейшего выражения
    assert calc.calc("1+1") == 2
def test_unar_minus():
    #отрицательное число с унарным минусом
    assert calc.calc("1+-2") == -1
def test_prio():
    #приоритетность операций
    assert calc.calc("2+3*4") == 14
def test_neg_num_mult():
    #умножение отрицательных чисел
    assert -2 * -3 == 6
def test_space():
    #игнорирование пробелов
    assert 10 / 4 == 2.5
def test_unar_signs():
    #сложное выражение с унарными плюсами и минусами
    assert calc.calc("-3++10*-2/+4") == -8
def test_float():
    #оценка соответствия
    assert abs(calc.calc("-1 * 4.25267/-1.02 + 0") - 4.16928431372549) <= 0.0000000001

#errors

def test_err_incor(capsys):
    #обработка ошибки ввода неизвестного символа
    with pytest.raises(SystemExit):
        calc.calc("2+a")
    cap = capsys.readouterr()
    assert cap.err == 'invalid syntaxis'

def test_err_emp(capsys):
    #обработка ошибки ввода пустой строки
    with pytest.raises(SystemExit):
        calc.calc("")
    cap = capsys.readouterr()
    assert cap.err == 'empty string'
def test_err_skip_num(capsys):
    #обработка ошибки пропущенного операнда
    with pytest.raises(SystemExit):
        calc.calc("2*/3")
    cap = capsys.readouterr()
    assert cap.err == 'invalid syntaxis'
def test_err_skip_op(capsys):
    #обработка ошибки пропущенного оператора
    with pytest.raises(SystemExit):
        calc.calc("2+1 2")
    cap = capsys.readouterr()
    assert cap.err == 'skipped operator'

def test_err_zero(capsys):
    #обработка деления на ноль
    with pytest.raises(SystemExit):
        calc.calc("1/0")
    cap = capsys.readouterr()
    assert cap.err == 'zero division error'