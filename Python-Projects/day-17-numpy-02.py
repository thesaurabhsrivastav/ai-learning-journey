import numpy as np

marks = np.array([70, 80, 90, 95, 85])

print(marks[1:4]) # [80, 90, 95, 85]

print(marks.ndim)

students = np.array([
    [70, 80, 90],
    [60, 75, 85]
])

print(students.ndim) #number of dimensions

print(students.shape) #Shape of array like 2x3

numbers = np.array([1, 2, 3])

print(numbers.dtype) #Data Type

import numpy as np

marks = np.array([
    [70, 80, 90],
    [60, 75, 85],
    [88, 92, 95]
])

print("Dataset:")
print(marks)

print("Shape:", marks.shape)
print("Dimensions:", marks.ndim)

print("First Student:", marks[0])