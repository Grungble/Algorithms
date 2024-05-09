import math
from matplotlib import pyplot as plt

def func_one_linear(x:int):
    return x 
def func_two_quad(x:int):
    return x*x
def func_three_exp(x:int):
   return x**x
def func_four_log(x:int):
    return int (math.log2(x))
if __name__ =='__main__':
    MIN_X = 1
    MAX_X = 4
    x_range = [x for x in range(MIN_X, MAX_X + 1)]
    print( x_range)

    y_range_linear = []
    y_range_quad = []
    y_range_exp = []
    y_range_log = []

    for x in x_range:
        y_lin = func_one_linear(x)
        y_range_linear.append(y_lin)

        y_quad = func_two_quad(x)
        y_range_quad.append(y_quad)

        y_exp = func_three_exp(x)
        y_range_exp.append(y_exp)
        
        y_log = func_four_log(x)
        y_range_log.append(y_log)

    plt.plot( x_range, y_range_linear, marker = 'o', label = 'linear')
    plt.plot(x_range, y_range_quad, marker='*', label = 'quadratic')
    plt.plot(x_range, y_range_exp, marker = '.', label='exponential')
    plt.plot(x_range, y_range_log, marker = 'x', label = 'logrithmic')
    
    plt.legend(loc='upper left')

    plt.show()

