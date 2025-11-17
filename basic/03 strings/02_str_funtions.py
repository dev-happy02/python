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
