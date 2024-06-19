"""
The typing module in Python provides a way to specify types for variables, function parameters, and return values.
This can help improve code readability, enable type checking,
and provide better support for IDEs and tools that offer code completion and static analysis.
Here are some of the most commonly used features of the typing module:
"""

x = 5
y: int = 10
print(f"value of x : {x} & value of y : {y}")

from typing import List, Tuple, Union, Optional, Any, Tuple, TypedDict, TypeVar, Generic, NewType


def add(a: int, b: int) -> int:
    return a + b


def greet(names: List[str]) -> None:
    for name in names:
        print(f"value of name is : {name} ")


def get_coordinates() -> Tuple[float, float]:
    return 40.7128, -74.0060


def process_data(data: Union[List[int], str]) -> Union[str, int]:
    if isinstance(data, list):
        return sum(data)
    elif isinstance(data, str):
        return len(data)
    else:
        raise ValueError("Unsupported type")


def fetch_data(user_id: int) -> Optional[dict]:
    if user_id == 0:
        return None
    return {"id": user_id, "name": "xyz"}


"""
Any Type
The Any type allows any type of value, effectively disabling type checking for that variable.

"""


def print_value(value: Any) -> None:
    print(f"printing the value  : {value}")


Coordinates = Tuple[float, float]
User = Tuple[int, str, Coordinates]


def get_user() -> User:
    return (1, "Alice", (40.7128, -74.0060))


"""
TypedDict
TypedDict allows you to specify the types of dictionary keys and values.
"""


class UserDict(TypedDict):
    id: int
    name: str
    age: int


def create_user() -> UserDict:
    return {"id": 1, "name": "Alice", "age": 30}


"""
Generics
Generics allow you to define classes and functions that can work with any type.

"""

T = TypeVar('T')


class Stack(Generic[T]):
    def __init__(self):
        self.items: List[T] = []

    def push(self, item: T) -> None:
        self.items.append(item)

    def pop(self) -> T:
        return self.items.pop()


# Example usage
stack = Stack[int]()
stack.push(1)
stack.push(2)
print(stack.pop())

"""
NewType
NewType creates distinct types based on existing types, useful for type-checking.
"""

print("=========================  NewType  =======================")

UserId = NewType('UserId', int)


def get_user_name(user_id: UserId) -> str:
    return f"User_{user_id}"


user_id = UserId(10)
print(get_user_name(user_id))
