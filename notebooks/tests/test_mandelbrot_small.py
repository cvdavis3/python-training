import numpy as np
from mandlebrot import mandelbrot

def test_mandelbrot_small():
    x = np.linspace(-2.25, 0.75, 10)
    y = np.linspace(-1.25, 1.25, 10)
    output = mandelbrot(x, y, 100, False)
    assert output.shape == (10, 10)