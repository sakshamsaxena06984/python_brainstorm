"""

A decorator in Python is a special function that modifies the behavior of another function or
 method without changing its actual code. Decorators are widely used for tasks such as logging,
 enforcing access control, instrumentation, memoization, and more.

How Decorators Work:
A decorator is a higher-order function that takes a function as an argument and returns a modified version of that function.
They are often used with the @decorator_name syntax.

A **decorator** in Python is a special function that **modifies the behavior of another function or method** without changing its actual code. Decorators are widely used for tasks such as logging, enforcing access control, instrumentation, memoization, and more.

---

## **How Decorators Work:**
- A decorator is a **higher-order function** that takes a function as an argument and returns a modified version of that function.
- They are often used with the `@decorator_name` syntax.

---

## **Basic Example Without `@` Syntax:**
```python
def decorator(func):
    def wrapper():
        print("Before the function call")
        func()
        print("After the function call")
    return wrapper

def say_hello():
    print("Hello!")

# Manually applying the decorator
decorated_func = decorator(say_hello)
decorated_func()
```

**Output:**
```
Before the function call
Hello!
After the function call
```

---

## **Using Decorators with `@` Syntax (Syntactic Sugar):**
```python
def decorator(func):
    def wrapper():
        print("Before the function call")
        func()
        print("After the function call")
    return wrapper

@decorator  # Applying the decorator
def say_hello():
    print("Hello!")

say_hello()
```

**Output:**
```
Before the function call
Hello!
After the function call
```

---

## **How Decorators Work Internally:**
1. The `@decorator` syntax applies the `decorator` function to `say_hello`.
2. `decorator` returns the `wrapper` function.
3. The original `say_hello` is replaced with the `wrapper` function.

---

## **Decorators with Arguments:**
```python
def repeat(n):
    def decorator(func):
        def wrapper():
            for _ in range(n):
                func()
        return wrapper
    return decorator

@repeat(3)  # Decorator with arguments
def greet():
    print("Hello!")

greet()
```

**Output:**
```
Hello!
Hello!
Hello!
```

---

## **Common Built-in Decorators in Python:**

### 1. **`@staticmethod`**
- Used to define a method that doesn't need `self` or `cls`.
```python
class Math:
    @staticmethod
    def add(x, y):
        return x + y

print(Math.add(3, 5))  # Output: 8
```

---

### 2. **`@classmethod`**
- Used for class-level methods that operate on the class itself (`cls`).
```python
class Person:
    count = 0

    @classmethod
    def increment_count(cls):
        cls.count += 1

Person.increment_count()
print(Person.count)  # Output: 1
```

---

### 3. **`@property`**
- Used to create **read-only** properties.
```python
class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

p = Person("Alice")
print(p.name)  # Output: Alice
# p.name = "Bob"  # This will raise an AttributeError
```

---

## **Multiple Decorators (Stacking Decorators):**
```python
def decorator1(func):
    def wrapper():
        print("Decorator 1")
        func()
    return wrapper

def decorator2(func):
    def wrapper():
        print("Decorator 2")
        func()
    return wrapper

@decorator1
@decorator2
def say_hello():
    print("Hello!")

say_hello()
```

**Output:**
```
Decorator 1
Decorator 2
Hello!
```

---

## **Key Takeaways:**
- **Decorators** modify a function’s behavior without changing its code.
- They can be used with the `@` symbol for cleaner syntax.
- Common use cases: Logging, authentication, input validation, measuring execution time, etc.

Would you like to see more advanced examples like **decorators for timing functions** or **class-based decorators**? 😊
"""
def lower_decor(function):
    def wrapper():
        func=function()
        new_func=func.lower()
        print(f"inside the first function : {new_func}")
        return new_func
    return wrapper

def spliter_decor(function):
    def wrapper():
        func=function()
        new_func=func.split()
        print(new_func)
        return new_func
    return wrapper

@spliter_decor
@lower_decor
def hello():
    return 'Hello World'

if __name__=='__main__':
    print(hello())
