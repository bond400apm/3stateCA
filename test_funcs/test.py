import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 


import lib.tristateca as ca


def test_decimal_converter():
    rule_number = 8
    in_binary = ca.decimal_converter(rule_number,3)
    assert in_binary=='000000022'


def test_lookup_table():
    Rule = 8
    keys = (2,2)
    Result = int(ca.look_up_table(Rule)[keys])
    assert Result==2


if __name__ == "__main__":
    test_decimal_converter()
    test_lookup_table()
    print('No error found! Good job!')
