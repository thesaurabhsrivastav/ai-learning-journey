numbers = (10, 20, 30) #Tupples Can not be changed i.e Immutable where as Lists can be change they are mutable.

print(numbers[0])
print(numbers[1])

#Packing of a tupple
point = (4, 5)
#Unpacking of a tupple
x, y = point

print(x)
print(y)

#Sets in python
numbers = {1, 2, 2, 3, 3, 4}
print(numbers)
numbers.add(5)
numbers.remove(2)
numbers = {1, 2, 3}

print(2 in numbers) #True of False
a = {1, 2, 3}
b = {3, 4, 5}

print(a | b) #Union of Sets
print(a & b) #Intersection of Sets
print(a - b) #Difference of sets

#Return multiple values from set
def calculate(a, b):

    return a + b, a - b

sum_value, diff_value = calculate(10, 5)

print(sum_value)
print(diff_value)