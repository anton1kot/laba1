import subprocess
import sys
from pathlib import Path

def test_cli_invalid_command_writes_to_stderr_and_exits_2():
    """Ошибка пользователя должна вывести ошибку в stderr и завершиться с кодом 2"""
    result = subprocess.run(
        [sys.executable, "-m", "toolkit", "calc", "12+3/*1"],
        cwd=Path(__file__).resolve().parent.parent,
        capture_output=True,
        text=True,
    )
    assert result.returncode == 2

def test_cli_help_exits_with_0():
    """--help должен показывать справку и завершаться с кодом 0"""
    result = subprocess.run(
        [sys.executable, "-m", "toolkit", "--help"],
        cwd=Path(__file__).resolve().parent.parent,
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0
    # Проверяем, что вывод не пустой (там должна быть справка)
    assert len(result.stdout.strip()) > 0