from sure import *

def ez_test():
    (4).should.eql(2+2)

def failing_test():
    ("yo wasap G").shouldnt.eql(3)