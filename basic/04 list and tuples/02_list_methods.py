a = ["happy", 3245, "apple", 34.76, False]
print(a)
 
a.append("swaraj")
print(a)


numbers = [23, 4, 5, 87, 11, 34]
print("Original:", numbers)

# 1. insert() – add element at given index
numbers.insert(1, 15)
print("1. insert():", numbers)

# 2. remove() – removes first occurrence
numbers.remove(5)
print("2. remove():", numbers)

# 3. pop() – remove element (default last)
numbers.pop()
print("3. pop():", numbers)

# 4. sort() – sort list ascending
numbers.sort()
print("4. sort():", numbers)

# 5. reverse() – reverse list
numbers.reverse()
print("5. reverse():", numbers)

# 6. count() – count occurrences
print("6. count(5):", numbers.count(5))

# 7. index() – get index of element
# (10 is not in list, so using element 15)
print("7. index(15):", numbers.index(15))

# 8. extend() – add multiple elements
numbers.extend([50, 60])
print("8. extend():", numbers)

# 9. clear() – remove all elements
numbers.clear()
print("9. clear():", numbers)
