import random
import numpy as np
from matplotlib import pyplot as plt

#Convert decimal number to binary or ternary
def decimal_converter(Number,state=2):
    states = 8
    if state == 3:
        states = 9
    Converted = str(np.base_repr(Number,state))
    Converted_length = len(Converted)
    if Converted_length != states:
        padding = states - Converted_length
        Converted = '0'*padding + Converted
    return Converted

#Create the look up table for a certain rule
def look_up_table(Rule):
    neighborhoods = [(2,2),(2,1),(2,0),(1,2),(1,1),(1,0),(0,2),(0,1),(0,0)]
    Neighbor = decimal_converter(Rule,3)
    Table = {}
    for i in range(9):
        key = neighborhoods[i]
        value = Neighbor[i]
        Table.update({key:value})
    return Table  

#This is the class of Cellular
class CellularAutomata(object):
    #This stores the configure, rule number inforation
    def __init__(self,Rule_number,initial_condition):
        self.initial = initial_condition
        self.Rule = Rule_number
        self.current_config = initial_condition
        self._length = len(initial_condition)
        self.config = [initial_condition]
        
    #This tells the Cellular how to evolve
    def evolve(self):
        last_figure = self.current_config 
        current_figure = []
        for i in range(self._length):
            neighbor = (last_figure[i-1],last_figure[i]) #periodic boundary
            value = int(look_up_table(self.Rule)[neighbor])
            current_figure.append(value)
        self.current_config = current_figure
        self.config.append(self.current_config)      
        


