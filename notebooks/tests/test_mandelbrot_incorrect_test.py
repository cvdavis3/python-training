import numpy as np
from mandlebrot import mandelbrot

def test_mandelbrot_incorrect_test():
    x = np.linspace(-1.5, -2.0, 10)
    y = np.linspace(-1.25, 1.25, 10)
    output = mandelbrot(x, y, 100, False)
    assert np.all(output == 0.0)