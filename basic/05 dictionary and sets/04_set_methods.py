# Creating a set
numbers = {10, 20, 30, 40}
print("Original Set:", numbers)

# 1. add() – add single element
numbers.add(50)
print("1. After add(50):", numbers)

# 2. update() – add multiple elements
numbers.update([60, 70])
print("2. After update([60, 70]):", numbers)

# 3. remove() – remove element (error if not found)
numbers.remove(20)
print("3. After remove(20):", numbers)

# 4. discard() – remove element (no error if not found)
numbers.discard(100)   # No error
print("4. After discard(100):", numbers)

# 5. pop() – removes random element
numbers.pop()
print("5. After pop():", numbers)

# 6. clear() – remove all elements
temp = numbers.copy()
temp.clear()
print("6. After clear():", temp)

# 7. union() – combine sets
a = {1, 2, 3}
b = {3, 4, 5}
print("7. union:", a.union(b))

# 8. intersection() – common elements
print("8. intersection:", a.intersection(b))

# 9. difference() – items in a not in b
print("9. difference:", a.difference(b))

# 10. copy() – copy a set
copy_set = a.copy()
print("10. copy:", copy_set)
