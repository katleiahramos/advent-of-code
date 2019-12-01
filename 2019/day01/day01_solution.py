import math
import numpy

def txt_to_module_arr(file_name):
    arr = numpy.genfromtxt(file_name)
    return arr

def calculate_fuel_per_module(mass):
    return numpy.floor( mass / 3) - 2

def calculate_total_fuel(feulArr):
    sum = 0
    for i in fuelArr:
        sum += i
    return sum

module_arr = txt_to_module_arr("input.txt")
fuelArr = calculate_fuel_per_module(module_arr)
return calculate_total_fuel(fuelArr)
