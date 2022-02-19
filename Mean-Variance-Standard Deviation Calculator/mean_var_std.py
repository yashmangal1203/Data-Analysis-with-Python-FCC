import numpy as np


def calculate(list1):
    if len(list1) > 9 or len(list1) < 9:
        raise ValueError("List must contain nine numbers.")
    else:
        array = np.array(list1).reshape((3, 3))
        maindict = {
            "mean": [list(array.mean(axis=0)), list(array.mean(axis=1)), array.mean()],
            "variance": [list(array.var(axis=0)), list(array.var(axis=1)), array.var()],
            "standard deviation": [list(array.std(axis=0)), list(array.std(axis=1)), array.std()],
            "max": [list(array.max(axis=0)), list(array.max(axis=1)), array.max()],
            "min": [list(array.min(axis=0)), list(array.min(axis=1)), array.min()],
            "sum": [list(array.sum(axis=0)), list(array.sum(axis=1)), array.sum()],
        }
    return maindict


print(calculate([1, 2, 3, 4, 5, 6, 7, 8, 9]))
