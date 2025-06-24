
print("=== 'is' Operator Examples ===")
# Identity comparison
a = [1, 2, 3]
b = [1, 2, 3]  
c = a

print(f"a is b: {a is b}")  # False - different objects
print(f"a is c: {a is c}")  # True - same object
print(f"a == b: {a == b}")  # True - same content

# None comparison (correct usage)
value = None
print(f"value is None: {value is None}")  # True

print("\n=== 'in' Operator Examples ===")
# Membership testing
numbers = [1, 2, 3, 4, 5]
print(f"3 in numbers: {3 in numbers}")  # True
print(f"6 in numbers: {6 in numbers}")  # False

# String membership
text = "Hello World"
print(f"'World' in text: {'World' in text}")  # True
print(f"'world' in text: {'world' in text}")  # False

# Dictionary membership (checks keys by default)
data = {'name': 'John', 'age': 30}
print(f"'name' in data: {'name' in data}")  # True
print(f"'John' in data.values(): {'John' in data.values()}")  # True