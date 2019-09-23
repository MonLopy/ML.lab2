
import matplotlib.pyplot as plt


def func(x):
    y = (x - 5) ** 2
    return y


def pohidna(y):
    z = 2 * (y - 5)
    return z


def plot():
    a = []
    b = []
    for x in range(-50, 50, 1):
        y = (x - 5) ** 2
        a.append(x)
        b.append(y)
    plt.title("Our function")
    plt.plot(a, b)
    plt.show()


def grad():
    z = []
    b = []
    for x in range(-50, 50, 1):
        y = (x - 5) ** 2
        z.append(x)
        b.append(y)
    plt.title("Our function")
    plt.plot(z, b)
    x = 0
    s = []
    a = []
    step = 0.01
    eps = 10e-9
    for i in range(1, 1000):
        x_new = x - step * pohidna(x)
        y_new = func(x)
        a.append(x_new)
        s.append(y_new)
        if abs(x_new - x) <= eps:
            plt.scatter(x_new, y_new, color="r")
            plt.show()
            return s
        x = x_new

    return s



if __name__ == "__main__":

    print(func(2))
    print(pohidna(2))
    data = grad()
    print(data)
