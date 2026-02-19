import numpy as np
import pandas as pd

from sklearn.datasets import load_iris

iris = load_iris(as_frame=True)
df = iris.frame.copy()                   # містить target
df["species"] = df["target"].map(lambda i: iris.target_names[i])

df.head()
