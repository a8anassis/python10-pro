"""**kwargs** is a special syntax in Python that allows you to pass a variable number
of keyword arguments to a function. It is often used when you want to create functions
 that can accept any number of named arguments, making your code more flexible and reusable.
 """


def build_profile(firstname: str, lastname: str, **kwargs) -> dict:
    """Build a dictionary containing everything we know about a user."""
    profile = { "firstname": firstname, "lastname": lastname}

    for key, value in kwargs.items():
        profile[key] = value

    return profile

def print_profile(**kwargs) -> None:
    """Prints the user profile information."""

    if not kwargs:
        print("No profile information provided.")
        return

    for key, value in kwargs.items():
        print(f"{key}: {value}")

def main() -> None:
    user_profile = build_profile("Andreas", "Androutsos", age=20, city="Athens" )
    print_profile(**user_profile)
    # Output: {'firstname': 'Andreas', 'lastname': 'Androutsos', 'age': 20, 'city': 'Athens'}


if __name__ == "__main__":
    main()