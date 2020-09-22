# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.6.0
#   kernelspec:
#     display_name: 'Python 3.8.0 64-bit (''pyproject'': venv)'
#     name: python_defaultSpec_1600764602575
# ---

# + tags=[]
import matplotlib.pyplot as plt
import numpy as np
from typing import Iterator
# %matplotlib inline
# -

# ## Basic Usage of matplotlib  
# Note that using plt.subplots below is equivalent to using  
# `fig = plt.figure()` and then `ax = fig.add_subplot(111)`

# Data for plotting
t = np.arange(0.0, 4.0, 0.01)
s = 1 + np.sin((5 * 2)* np.pi * t)

fig, ax = plt.subplots()
ax.plot(t, s)
ax.set(xlabel='time (s)', ylabel='voltage (mV)', title='Sine Wave')
ax.grid()


def fib(n: int) -> Iterator[int]:
    a, b = 0, 1
    while a < n:
        yield a
        a, b = b, a+b
