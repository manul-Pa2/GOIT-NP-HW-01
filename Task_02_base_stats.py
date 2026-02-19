import numpy as np
import pandas as pd

from sklearn.datasets import load_iris

iris = load_iris(as_frame=True)

df[iris.feature_names].describe()      # <-- можливо помиляюсь, саме ця функція витягує базові стати
