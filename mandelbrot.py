import numpy as np
import matplotlib.pyplot as plt

# counts the number of iterations until the function diverges or
# returns the iteration threshold that we check until
def isDivergent(c, maxIt):
    z = complex(0, 0)
    iteration = 0

    while(abs(z) < 4 and iteration < maxIt):
        z = z*z + c

        iteration += 1
        
    return iteration


def mandelbrot(maxIt, realsFrom, realsTo, complexFrom, complexTo, xPixels = 1000, yPixels = 1000):
    realAxis = np.linspace(realsFrom, realsTo, xPixels)
    complexAxis = np.linspace(complexFrom, complexTo, yPixels)
    
    plane = np.empty((xPixels, yPixels))

    for i in range(xPixels):
        for j in range(yPixels):
            x = realAxis[i]
            y = complexAxis[j]
            c = complex(x, y)

            plane[i, j] = isDivergent(c, maxIt)

    plt.imshow(plane.T, interpolation="nearest")
    plt.show()


# mandelbrot(400, -2., 1., -1.5, 1.5)
mandelbrot(400, -0.22, -0.219, -0.70, -0.699)