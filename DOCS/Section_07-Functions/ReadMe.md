# Section 01 | Functions #

## Introduction to function ##

* group code into reusable blocks
* the code is executed only when called.
* based on the don't repeat yourself (DRY) principle
    * Organize similar logic together
    * change logic in one place.
* Basic syntax

```python
def output_welcome_text():
    print("Welcome")
```
* The function defination starts with `def` keywords.
* Followed by the function name, `output_welcome_text` in the above example
* followed by `()`, which can optionally have parameters to pass to the function
* at the end we should have `:`,  to tell python interpreter, that the function code block will follow.
* finally all the code of the function indented 4 space / 1 tab.
* Naming a function should 
    * follow snake case, like `output_welcome_text`, the words are seperated by `_`.
    * be in lower case
    * 79 char is the limit of function name
    * Must start with a letter, `a-z`
    * number can also be present in the name, but should not be first character.
* We can called the function, by just passing the function name, `output_welcome_text`, followed by `()`, i.e. `output_welcome_text()`

## Function DocStrings ##

* DocStrings are documentation for the function.
* It should be short and describe what the function does and also returns.
* It helps in creating automatic documentation.
* DocStrings are represented by `"""This is a docstring"""`.
* Should be at the first line after the function name.
* It should be indented with the function block.
* A sample function with DocStrings

```python
def output_welcome_text():
    """This is a docString."""
    print("Welcome")
```

## Arguments and Parameters ##

### What are arguments & parameters? ###

* Allow passing of data to and from function.
* This helps in using the same function logic, but with different inputs.

### Difference between argument & parameters? ###

* It is used interchangeably.
* Parameters - names that appear in a function defination.
    * example : `def output_welcome_text(name):`
    * multiple parameters are also possible, `def output_welcome_text(name, age, location):`
    * `,` is used to seperate parameters.
    * Using the paramenters, inside the function, it can be used just like a variable.
    ```python
    def output_welcome_text(name):
        print(f"Welcome {name}")
    ```
* arguments - describe values passed to a function when called.
    * You can call the above function with arguments, `output_welcome_text("Mark")`

### How to define parameters? ###
* Parameters - names that appear in a function defination.
    * example : `def output_welcome_text(name):`
    * multiple parameters are also possible, `def output_welcome_text(name, age, location):`
    * `,` is used to seperate parameters.
    * Using the paramenters, inside the function, it can be used just like a variable.
    ```python
    def output_welcome_text(name):
        print(f"Welcome {name}")
    ```
### How to pass arguments? ###
* arguments - describe values passed to a function when called.
    * You can call the above function with arguments, `output_welcome_text("Mark")`
* we multiple arguments are passed, it should pass the value as per the parameter order.
* this is also known as positional arguments

```python
def output_welcome_text(name, age, location):
        print(f"Welcome {name}. You are {age} and from {location}")

output_welcome_text("Mark", 39, "London")
```

* We can use KeyWord arguments. We specify the parameters and the value to be assigned to it.

```python
def output_welcome_text(name, age, location):
        print(f"Welcome {name}. You are {age} and from {location}")

output_welcome_text(location= "London", name = "Mark", age=39)
```

* Positional and keyword arguments may be combined.
    * positional arguments must appear first followed by keyword.

### Default Parameters ###

```python
def output_welcome_text(name, age, location="london"):
        print(f"Welcome {name}. You are {age} and from {location}")

output_welcome_text(name = "Mark", age=39)
output_welcome_text("Mark", 39, "Delhi")
```

* We can assign default values to parameters in the function defination.
* It will use this value if the caller function does not pass the arguments.
* if the caller passes a value, we will use the same value passed.
* default parameters should always come at the end

### Multi Line Argument ###
* We can have multi line parameters in a function like this.
```python
def output_welcome_text(first_name, 
                        last_name, 
                        age, 
                        location, 
                        returning_user=True):
    """Output welcome text with user details"""
    if returning_user:
        msg_start = f"Welcome back {first_name} {last_name} "
    else:
        msg_start = f"Welcome {first_name} {last_name}"

    msg = f"{msg_start} You are {age} and from {location}."
    print(msg)
```

* We can call the above function with multi line argument
```python
output_welcome_text(
    "Mark", 
    "W", 
    age=31, 
    location="london"
)
```

## Function Scope ##

* It tells us where the variable can be used or accessed.
* This is possible by identifying where the variable is defined.
* Scope of a variable helps in 
    * debugging - we can just debug a small piece of code where the variable is accessibale.
    * security - As the variables are scoped, it limits its access.
* consider the below example.

```python
def function_a():
    var_one = "one"
def function_b():
    var_two = "two"

var_three = "three"
```

* In the above code,
    * `var_three` is in the global scope, which means it can be accessed from anywhere.
    * even the function `function_a` & `function_b` is in the global scope.
    * there is also local scope, the variable `var_one` & `var_two` are in the local scope of the function.
    * the variable `var_one` & `var_two` are not accessible from the global scope.

```python
def print_greeting(name):
    """print a welcome message with given name"""
    message = f"Welcome {name}"


print_greeting("Mark")
print(message)

```

* In the above code we will get the error `NameError: name 'message' is not defined`, as it is not in scope.

## Return Statement ##