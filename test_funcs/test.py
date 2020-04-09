import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 


import lib.tristateCA as CA


def Test_Decimal_Converter():
    Rule_number = 8
    In_Binary = CA.Decimal_Converter(Rule_number,3)
    print(In_Binary)


def test_Lookup_table():
    Rule = 8
    keys = (2,2)
    Result = CA.Look_up_table(Rule,keys)
    print(Result==2)


if __name__ == "__main__":
    Test_Decimal_Converter()
    test_Lookup_table()
