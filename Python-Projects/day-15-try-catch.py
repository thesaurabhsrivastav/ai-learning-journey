try:
    file = open("data.txt")

except FileNotFoundError:
    print("File missing")

finally:
    print("Execution completed")