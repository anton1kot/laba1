from src.toolkit import calc

def test_simple_add():
    assert calc.calc("1+1") == 2
def test_complex_add_and_sub():
    assert calc.calc("1+1-3") == -1
def test_prio():
    assert calc.calc("1+7*3") == 22
def test_unar_signs():
    assert calc.calc("-3++10*-2/+4") == -8
def test_space_and_float():
    assert calc.calc("-1 * 4.25267/-1.02 + 0") == 4.16928431372549

import sys
import pytest

def test_err_incor():
    with pytest.raises(SystemExit) as e:
        calc.calc("!2+1")
    assert e.type == SystemExit
    assert e.value.code == 'invalid syntaxis'

def test_err_emp():
    with pytest.raises(SystemExit) as e:
        calc.calc("")
    assert e.type == SystemExit
    assert e.value.code == 'empty string'

def test_err_skip():
    with pytest.raises(SystemExit) as e:
        calc.calc("2+1 2")
    assert e.type == SystemExit
    assert e.value.code == 'skipped operand'

def test_err_zero():
    with pytest.raises(SystemExit) as e:
        calc.calc("-2/8/0")
    assert e.type == SystemExit
    assert e.value.code == 'zero division error'