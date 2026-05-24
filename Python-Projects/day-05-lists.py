numbers = [10, 20, 30, 40]

print(numbers[0])
print(numbers[2])
print(numbers[-1]) #Last Index Number
numbers = [10, 20, 30, 40, 50]

print(numbers[1:4]) #Including 1st index and excluding 4th Index

numbers = [1, 2, 3]

numbers.append(4)

print(numbers)

#Add at specific index
numbers.insert(1, 100)
numbers.remove(2) #Remove by Value
numbers.pop(1) #Remove By Pop

numbers = [10, 20, 30]
#Loop in Lists
for num in numbers:
    print(num)

fruits = ["apple", "banana"]

print("apple" in fruits)