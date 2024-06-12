name = input("Name: ")
#Define lists of names
names = ["jann", "railey", "thomas", "eddie"]
#tuple
coordinates = (100.00, 89.00)
#set
s = set()
#ading elemts on set
s.add(1)
s.add(2)
s.add(3)
s.add(4)
s.add(1)

print(f"The set has {len(s)} elements.")
print(s)
print(f"Hello, {name}")
print(names)

names.append(name)

names.sort()

print(names)

n = int(input("Number: "))

if n > 0:
    print("n is positive")
elif n < 0:
    print("n is negative")
else:
    print("n is zero")