# Python 

```py

print("Hello World");


```

```py
print(''' Python is a high-level, general-purpose programming language that is easy to read, easy to write, and widely used for web development, data science, machine learning, automation, and many other applications.
      
Why it’s popular:

Simple English-like syntax
Huge libraries (NumPy, Pandas, Django, etc.)
Works everywhere (Windows, Mac, Linux)
Easy for beginners, powerful for experts ''')
```

```py
# about myself (single line comment)


print("hii this is happy swaraj")



#  multi-line comments in two ways


"""
happy swaraj
12205899
9128730395
dev_happy02
"""

'''
happy swaraj
12205899
9128730395
dev_happy02
'''
```


```py

a= int(input("enter first number "))
b= int(input("enter second number "))

sum = a+b
print("sum is " , sum)
```
```py
a = 1        # a is an integer

b = 5.22     # b is a floating point number

c = "Happy"  # c is a string

d = False    # d is a boolean variable

e = None     # e is a none type variable

print(a)
print(b)
print(c)
print(d)
print(e)


# Ruels..

# Variable cannot start with a number.
# Can contain letters, digits, and underscore (_) only.
# No spaces allowed.
# Case-sensitive (age ≠ Age).
# Keywords cannot be used as variable names.
# No special characters allowed (like @, #, -, $).
# Name should be meaningful.
```



### Oerators



#### Arithmetic Operators
```py
a = 10
b = 3

print(a + b)   # Addition -> 13
print(a - b)   # Subtraction -> 7
print(a * b)   # Multiplication ->30
print(a / b)   # Division -> 3.333
print(a % b)   # Modulus -> 1
print(a ** b)  # Exponent -> 1000
print(a // b)  # Floor Division -> 3
```


#### Assignment Operators
```py

x = 5
print(x)

x += 2   # x = x + 2 -> 7
print(x)

x -= 1   # x = x - 1 -> 6
print(x)

x *= 3   # x = x * 3 -> 18
print(x)

x /= 2   # x = x / 2 -> 9.0
print(x)

x %= 4   # x = x % 4 -> 1
print(x)

x **= 3  # x = x ** 3 -> 1
print(x)

x //= 2  # x = x // 2 -> 0
print(x)
```

#### Comparison Operators
```py
a = 10
b = 20

print(a == b)   # Equal -> False
print(a != b)   # Not equal -> True
print(a > b)    # Greater -> False
print(a < b)    # Less -> True
print(a >= b)   # Greater or equal -> False
print(a <= b)   # Less or equal -> True
```


#### Logical Operators
```py

x = True
y = False

print(x and y)  # AND ->  False
print(x or y)   # OR  ->  True
print(not x)    # NOT ->  False
```


#### Bitwise Operators
```py
a = 5    # 0101
b = 3    # 0011


print(a & b)   # AND ->  1
print(a | b)   # OR ->  7
print(a ^ b)   # XOR ->  6
print(~a)      # NOT ->  -6
print(a << 1)  # Left shift ->  10
print(a >> 1)  # Right shift ->  2
```

#### Membership Operators
```py
nums = [1, 2, 3, 4]


print(2 in nums)       # True
print(10 not in nums)  # True
print(1 not in nums)  # False
```


#### Identity Operators
```py
a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)      # True (same object)
print(a is c)      # False (same value, different object)

print(a is not c)  # True
```


### Strings


#### intro

```py

name = "happy"

print(name)
print(len(name)) 
print (name[0:])
print (name[:5])
print (name[2:4]) 
```

#### string funtions 
```py

text = "  Hello World Welcome to Python  "
print(text)

print(text.lower())
print(text.upper())
print(text.title())
print(text.capitalize())
print(text.strip())
print(text.lstrip())
print(text.rstrip())
print(text.replace("Python", "Programming"))
print(text.split())

words = ["Python", "is", "fun"]
print(" ".join(words))

print(text.find("World"))
print(text.count("o"))
print(text.startswith("  Hello"))
print(text.endswith("on"))
print("HeLLo".swapcase())
```

```py

text = "  Hello World Welcome to Python  "
print(text)

# 1. lower() - convert to lowercase
print(text.lower())

  
# 2. upper() - convert to uppercase
print(text.upper())


# 3. title() - first letter capital of each word
print(text.title())


# 4. capitalize() - first letter capital
print(text.capitalize())


# 5. strip() - remove spaces from both sides
print(text.strip())


# 6. lstrip() - remove left spaces
print(text.lstrip())


# 7. rstrip() - remove right spaces
print(text.rstrip())


# 8. replace() - replace words
print(text.replace("Python", "Programming"))


# 9. split() - convert string to list
print(text.split())


# 10. join() - join list into string
words = ["Python", "is", "fun"]
print(" ".join(words))


# 11. find() - return index of substring
print(text.find("World"))


# 12. count() - count occurrences
print(text.count("o"))


# 13. startswith()
print(text.startswith("  Hello"))


# 14. endswith()
print(text.endswith("on"))


# 15. swapcase() - change upper <-> lower
print("HeLLo".swapcase())
```


#### escape

```py
a = "hii my name is \n Happy Swaraj"

print(a)


b = "hii my name is \"Happy Swaraj\""
print(b)



c = "hii my name is \t Happy Swaraj "
print(c)
```

### list and tuples
#### list 
```py

a = ["happy", 3245, "apple", 34.76, False]

print(a)

a[0]= "swaraj" 
print(a)

print(a[4])  # print -> False
print(a[2:4])  # print -> apple, 34.76
```



#### list methods
```py

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
```





















