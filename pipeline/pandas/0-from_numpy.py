import numpy as np
import pandas as pd

def from_numpy(array):
    import string
    cols = list(string.ascii_uppercase[:arrayshape[1]])
    return pd.DataFrame(array, columns=cols)
