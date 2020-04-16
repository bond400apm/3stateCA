import random
import numpy as np
from matplotlib import pyplot as plt
import lib.tristateca as ca

if __name__ == "__main__":
    #Length of Cellular
    length = 100

    #Generate an initial condition
    initial_condition = []
    for i in range(length):
        initial_condition.append(random.randint(0,2))

    #Create a Cellular instance
    field = ca.CellularAutomata(127,initial_condition)

    #Let the Cellular evolve
    for i in range(100):
        field.evolve()
    #print(field.config) 

    #Make the plot
    plt.matshow(field.config)
    plt.colorbar()
    plt.show()

