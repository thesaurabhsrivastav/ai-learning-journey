for i in range(5):
    print("Hello")

for i in range(5):
    print(i)


for i in range(1, 6):
    print(i)

for i in range(0, 10, 2):
    print(i)

count = 1

while count <= 5:
    print(count)
    count += 1

for i in range(10):
    if i == 5:
        break

    print(i)

for i in range(5):

    if i == 2:
        continue

    print(i)

for i in range(3):

    for j in range(2):
        print(i, j)
    
number = int(input("Enter a number: "))

print("PRINT THE TABLE OF GIVEN NUMBER")
for i in range(1, 11):
    print(number, "x", i, "=", number * i)