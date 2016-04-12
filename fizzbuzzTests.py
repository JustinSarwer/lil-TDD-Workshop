from sure import *
from fizzbuzz import fizzbuzz

def test_fizzbuzz1ShouldEql1():
    fizzbuzz(1).should.eql(1)

def test_fizzbuzz3ShouldRetFizz():
    fizzbuzz(3).should.eql("Fizz")

def test_fizzbuzz5ShouldRetBuzz():
    fizzbuzz(5).should.eql("Buzz")

def test_fizzbuzz10ShouldRetBuzz():
    fizzbuzz(10).should.eql("Buzz")

def test_fizzbuzz15ShouldShouldRetFizzBuzz():
    fizzbuzz(15).should.eql("FizzBuzz")