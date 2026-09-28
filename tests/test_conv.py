import pytest

from toolkit import convert


def test_len():
    #конвертер длины
    assert convert.conv("1000 --from mm --to m") == 1

def test_mass():
    #конвертер массы
    assert convert.conv("1.5 --from kg --to g") == 1500
def test_reg():
    #проверка работы конверетера в верхнем регистре единиц
    assert convert.conv("1 --from MM --to Cm") == 0.1
def test_temp():
    #конвертер температуры
    assert convert.conv("-273.15 --from c --to k")==0

#errors

def test_err_incor_un(capsys):
    #ошибка ввода единиц
    with pytest.raises(SystemExit):
        convert.conv("2 --from mm --to sm")
    cap=capsys.readouterr()
    assert cap.err == 'incorrect unit'

def test_err_dif(capsys):
    #ошибка конвертации разных групп
    with pytest.raises(SystemExit):
        convert.conv("3 --from kg --to m ")
    cap=capsys.readouterr()
    assert cap.err == 'different units'

def test_err_inp(capsys):
    #ошибка некорректного ввода
    with pytest.raises(SystemExit):
        convert.conv("2 from c to f")
    cap=capsys.readouterr()
    assert cap.err == 'incorrect input'

def test_err_zero(capsys):
    #ошибка температуры ниже нуля
    with pytest.raises(SystemExit):
        convert.conv("-500 --from f --to c")
    cap=capsys.readouterr()
    assert cap.err == 'lower abs zero'