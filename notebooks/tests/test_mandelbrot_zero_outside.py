import numpy as np
from mandlebrot import mandelbrot

def test_mandelbrot_zero_outside():
    # The Mandelbrot set should be zero outside the "active" area
    x = np.linspace(1.5, 2.0, 10)
    y = np.linspace(1.5, 2.0, 10)
    output = mandelbrot(x, y, 100, False)
    assert np.all(output == 0.0)