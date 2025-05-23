import pytest
from calculator import sumar, restar, multiplicar, dividir

def test_sumar():
    assert sumar(2, 3) == 5
    assert sumar(-1, 1) == 0
    assert sumar(0, 0) == 0
    assert sumar(2.5, 3.5) == 6.0

def test_restar():
    assert restar(5, 3) == 2
    assert restar(0, 0) == 0
    assert restar(-1, -1) == 0
    assert restar(2.5, 1.5) == 1.0

def test_multiplicar():
    assert multiplicar(2, 3) == 6
    assert multiplicar(-1, 1) == -1
    assert multiplicar(0, 100) == 0
    assert multiplicar(2.5, 2) == 5.0

def test_dividir():
    assert dividir(6, 3) == 2
    assert dividir(-4, 2) == -2
    assert dividir(5.0, 2.0) == 2.5

def test_dividir_por_cero():
    assert dividir(5, 0) == "Error: División por cero"
    assert dividir(0, 0) == "Error: División por cero"