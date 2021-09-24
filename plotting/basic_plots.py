import numpy as np
import matplotlib.pyplot as plt


def basic1():
    # evenly sampled time at 200ms intervals
    t = np.arange(0., 5., 0.2)

    # red dashes, blue squares and green triangles
    plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
    plt.show()


def scatter():
    """You can use a dataframe/dictionary to make the scatterplots and just specify the keys
    """
    data = {'a': np.arange(50),
            'c': np.random.randint(0, 50, 50),
            'd': np.random.randn(50)}
    data['b'] = data['a'] + 10 * np.random.randn(50)
    data['d'] = np.abs(data['d']) * 100

    plt.scatter('a', 'b', c='c', s='d', data=data)
    plt.xlabel('entry a')
    plt.ylabel('entry b')
    plt.show()


def properties():
    x = np.linspace(0, 10, 101)
    y = np.float_power(x, 2.5)
    # line.set_antialiased(False)  # this makes it more pixelated/rough?
    line, = plt.plot(x, y)
    plt.setp(line, 'color', 'r', 'linewidth', 0.5, 'alpha', 0.5)
    plt.show()


def subplots():
    names = ['group_a', 'group_b', 'group_c']
    values = [1, 10, 100]

    # figsize is the (width, height) in inches. Dumb that it's width first when subplot is the other way
    plt.figure(figsize=(9, 3))

    # 131 means it is a 1x3 grid and we are editing the first one
    plt.subplot(131)
    plt.bar(names, values)
    # 132 means it is a 1x3 grid and we are editing the second one
    plt.subplot(132)
    plt.scatter(names, values)
    plt.subplot(133)
    plt.plot(names, values)
    plt.suptitle('Categorical Plotting')
    plt.show()


def multiple_axes():
    plt.figure(1)                 # the first figure
    plt.subplot(211)              # the first subplot in the first figure
    plt.plot([1, 2, 3])
    plt.subplot(212)              # the second subplot in the first figure
    plt.plot([4, 5, 6])

    plt.figure(2)                 # a second figure
    plt.plot([4, 5, 6])           # creates a subplot() by default

    plt.figure(1)                 # figure 1 current; subplot(212) still current
    plt.subplot(211)              # make subplot(211) in figure1 current
    plt.title('Easy as 1, 2, 3')  # subplot 211 title
    plt.clf()
    plt.show()


def text():
    x = np.linspace(0, 10, 101)
    y = np.float_power(x, 2.5)
    plt.plot(x, y)
    plt.text(5, 25, r'mytext')
    # text is placed in data coordinates by default

    # xy is the coordinate being pointed out
    # xytext is the location of the text annotating the point
    plt.annotate('i=14', xy=(x[14], y[14]), xytext=(x[14], y[14] + 20),
                 arrowprops=dict(facecolor='black', shrink=0.01),)

    # latex
    plt.title(r'$\sigma_i=15$')
    plt.show()


def log_axis():
    np.random.seed(19680801)

    # make up some data in the open interval (0, 1)
    y = np.random.normal(loc=0.5, scale=0.4, size=1000)
    y = y[(y > 0) & (y < 1)]
    y.sort()
    x = np.arange(len(y))
    plt.subplot(211)
    plt.plot(x, y)
    plt.title('normal axes')

    plt.subplot(212)
    plt.semilogx(x, y)
    plt.title('logx axes')
    plt.show()


log_axis()
