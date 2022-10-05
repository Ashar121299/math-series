

from math_series.math_series import fap, lucas, sum_series
import pytest

#test fappicioni
def test_fap0():
    actual=fap(0)
    expected=0
    assert actual == expected
def test_fap1():
    actual=fap(1)
    expected=1
    assert actual == expected
def test_fap2():
    actual=fap(2)
    expected=1
    assert actual == expected
def test_fap7():
    actual=fap(7)
    expected=13
    assert actual == expected
#test lucas
def test_lucas0():
    actual=lucas(0)
    expected=2
    assert actual == expected
def test_lucas1():
    actual=lucas(1)
    expected=1
    assert actual == expected
def test_lucas2():
    actual=lucas(2)
    expected=3
    assert actual == expected

# test sum series as fapiioni and lucas
def test_sum_series0():
    actual=sum_series(0,0,1)
    expected=0
    assert actual == expected 
def test_sum_series0L():
    actual=sum_series(0,2,1)
    expected=2
    assert actual == expected 


def test_sum_series1():
    actual=sum_series(1,0,1)
    expected=1
    assert actual == expected 
def test_sum_series1L():
    actual=sum_series(1,2,1)
    expected=1
    assert actual == expected 

def test_sum_series5():
    actual=sum_series(5,0,1)
    expected=5
    assert actual == expected 
def test_sum_series5L():
    actual=sum_series(5,2,1)
    expected=11
    assert actual == expected 

# test sum series as another type of series

def test_sum_seriesA0():
    actual=sum_series(0,3,2)
    expected=3
    assert actual == expected 
def test_sum_seriesA1():
    actual=sum_series(1,3,2)
    expected=2
    assert actual == expected 
def test_sum_seriesA6():
    actual=sum_series(6,3,2)
    expected=31
    assert actual == expected 

