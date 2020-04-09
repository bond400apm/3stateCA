import random
import numpy as np
from matplotlib import pyplot as plt
import lib.tristateCA as CA

if __name__ == "__main__":
    length = 100
    initial_condition = []
    for i in range(length):
        initial_condition.append(random.randint(0,2))

    field = CA.Cellular_Automata(127,initial_condition)
    for i in range(100):
        field.evolve()
    #print(field.config) 
    plt.figure(figsize=(12,12))
    plt.matshow(field.config)
    plt.colorbar()
    plt.show()

