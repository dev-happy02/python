marks = {
    "keys": "values",
    "happy": 97,
    "prince": 95,
    "abhi": 85,
    "rohit": 50,
    "nikita": 99
}

print("Original Marks Dictionary:", marks)

# 1. get() – most used
print("1. Get abhi:", marks.get("abhi"))

# 2. update() – update multiple values at once
marks.update({"happy": 98, "prince": 99})
print("2. After update():", marks)

# 3. Adding a new key
marks["rahul"] = 88
print("3. After adding 'rahul':", marks)

# 4. Updating an existing value
marks["rohit"] = 55
print("4. After updating 'rohit':", marks)

# 5. items()
print("5. Items:", marks.items())

# 6. pop() – remove a key
marks.pop("keys")
print("6. After pop('keys'):", marks)

# 7. popitem() – remove last inserted item
marks.popitem()
print("7. After popitem():", marks)

# 8. copy()
copy_marks = marks.copy()
print("8. Copy:", copy_marks)

# 9. clear()
marks.clear()
print("9. After clear():", marks)
