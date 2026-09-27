from src.toolkit import convert

def test_mass():
    assert convert.conv("1 --from g --to kg") == 0.001
def test_len_and_reg():
    assert convert.conv("1 --from MM --to Cm") == 0.1
def test_temp():
    assert abs(-457.87-convert.conv("1 --from k --to f"))<=0.01

import sys
import pytest

def test_err_incor_un():
    with pytest.raises(SystemExit) as e:
        convert.conv("2 --from mm --to sm")
    assert e.type == SystemExit
    assert e.value.code == 'incorrect unit'

def test_err_dif():
    with pytest.raises(SystemExit) as e:
        convert.conv("3 --from kg --to mm ")
    assert e.type == SystemExit
    assert e.value.code == 'different units'

def test_err_inp():
    with pytest.raises(SystemExit) as e:
        convert.conv("2 from c to f")
    assert e.type == SystemExit
    assert e.value.code == 'incorrect input'

def test_err_zero():
    with pytest.raises(SystemExit) as e:
        convert.conv("-500 --from f --to c")
    assert e.type == SystemExit
    assert e.value.code == 'lower abs zero'