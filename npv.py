import sys
import os
import math


def calculateNPV(time, discount, values):
    print time
    amm = -float(values[0])
    for i in range(1, time+1):
        div = float(values[i])/pow(1+discount,i)
        amm = amm + div

    return amm
    

if __name__ == "__main__":

    vet = sys.argv
    vet = vet[2:]
    print vet
    print calculateNPV(len(sys.argv)-3, float(sys.argv[1]), vet)
