from src.toolkit import convert

def test_mass():
    assert convert.conv("1 --from g --to kg") == 0.001
def test_len_and_reg():
    assert convert.conv("1 --from MM --to Cm") == 0.1
def test_temp():
    assert abs(-457.87-convert.conv("1 --from k --to f"))<=0.01

import sys
import pytest

def test_err_incor_un(capsys):
    with pytest.raises(SystemExit) as e:
        convert.conv("2 --from mm --to sm")
    cap=capsys.readouterr()
    assert cap.err == 'incorrect unit'

def test_err_dif(capsys):
    with pytest.raises(SystemExit) as e:
        convert.conv("3 --from kg --to mm ")
    cap=capsys.readouterr()
    assert cap.err == 'different units'

def test_err_inp(capsys):
    with pytest.raises(SystemExit) as e:
        convert.conv("2 from c to f")
    cap=capsys.readouterr()
    assert cap.err == 'incorrect input'

def test_err_zero(capsys):
    with pytest.raises(SystemExit) as e:
        convert.conv("-500 --from f --to c")
    cap=capsys.readouterr()
    assert cap.err == 'lower abs zero'