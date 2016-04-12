from sure import *
from fizzbuzz import fizzbuzz

def test_fizzbuzz1ShouldEql1():
    fizzbuzz(1).should.eql(1)

def test_fizzbuzz3ShouldRetFizz():
    fizzbuzz(3).should.equal("Fizz")