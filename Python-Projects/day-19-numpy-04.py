import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])

print(arr.shape) #O/P is (6,)

new_arr = arr.reshape(2, 3)

print(new_arr) 
"""
Output is [[1 2 3]
 [4 5 6]]
"""

arr = np.array([
    [1, 2],
    [3, 4]
])

print(arr.flatten()) # [1 2 3 4]

arr = np.zeros((2, 3))

print(arr)

"""
[[0. 0. 0.]
 [0. 0. 0.]]
"""

np.linspace(0, 10, 5) #[0.  2.5  5.  7.5 10.]
