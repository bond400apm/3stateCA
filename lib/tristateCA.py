import random
import numpy as np
from matplotlib import pyplot as plt


def Decimal_Converter(Number,state=2):
    states = 8
    if state == 3:
        states = 9
    Converted = str(np.base_repr(Number,state))
    Converted_length = len(Converted)
    if Converted_length != states:
        padding = states - Converted_length
        Converted = '0'*padding + Converted
    return Converted

def Look_up_table(Rule,keys):
    neighborhoods = [(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)]
    Neighbor = Decimal_Converter(Rule,3)
    Table = {}
    for i in range(9):
        key = neighborhoods[i]
        value = Neighbor[i]
        Table.update({key:value})
    return int(Table[keys])  


class Cellular_Automata(object):
    def __init__(self,Rule_number,initial_condition):
        self.initial = initial_condition
        self.Rule = Rule_number
        self.current_config = initial_condition
        self._length = len(initial_condition)
        self.config = [initial_condition]
        
    
    def evolve(self):
        last_figure = self.current_config 
        current_figure = []
        for i in range(self._length):
            neighbor = (last_figure[i-1],last_figure[i]) #periodic boundary
            current_figure.append(Look_up_table(self.Rule,neighbor))
        self.current_config = current_figure
        self.config.append(self.current_config)      
        


