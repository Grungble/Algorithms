from matplotlib import pyplot as plt

def f(x):
    return ((x**2)-1)

if __name__ == '__main__':
    plt.axhline( y=0 )
    plt.axhline( y=-1, color='red', linestyle='--' )
    plt.ylim(-2,2)

    x0 = 1.61803399
    iterations = 20
    val_list = []
    iter_list = [i for i in range(iterations)]

    for i in range(iterations):
        val_list.append(x0)
        x0 = f(x0)
    print(val_list)
    plt.plot(iter_list, val_list, color='green')








    # shoew
    plt.show()
