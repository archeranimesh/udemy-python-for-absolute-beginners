msg_prefix = "Welcome"
message = "hello"


def print_greeting(name):
    """print a welcome message with given name"""
    message = f"{msg_prefix} {name}"
    print(message)


print_greeting("Mark")
print(message)
