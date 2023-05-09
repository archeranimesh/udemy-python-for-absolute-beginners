# Section 05 | String Manipulation #

## Overview of using strings ##

* String formatting is nothing but creation of strings in Python.
* Injecting variables into the strings

### Four different approaches ###

* We can format the string in 4 different ways
    * Concatenation
        * It looks like this
        ```python
        name = "John"
        age = 31
        message = 'Hello ' +name + ' (' +str(age) + ')'     # Hello John (31)
        ```
        * This is approach is difficult to read, prone to error and very difficult to maintain.
        * This approach should be avoided.
    * Old style formatting (using %)
        * This is how it looks
        ```python
        name = "John"
        age = 31
        message = "Hello %s (%i)" %(name, age)
        ```
        * This approach can be deprecated.
        * Newer, cleaner options are available
        * This should be avoided in the new code.
        * Type conversion is automatic.
    * format function
        * this is how it looks
        ```python
        name = "John"
        age = 31
        message = 'Hello {} {}'.format(name, age)
        ```
        * The newer version.
        * It also supports conversion.
        * This is also backward compatiable.
    * Formatted string literals.
        * this is how it looks
        ```python
        name = "John"
        age = 31
        message = f'Hello {name} ({age})'
        ```
        * Cleanest, fastest approach
        * available in Python 3.6


## Format Function ##

* We have 3 ways to use the format function for string manipulation.
* The first approach is already known
```python
name = "animesh"
age = 41
# Standard message format
message = "Hello {} ({})".format(name, age)
```

* We can also change the argument order, by indexing them
```python
name = "animesh"
age = 41
# Change the argument order
message_2 = "Hello {1} ({0})".format(age, name)     # Hello 31 (animesh)
```

* We can also use kwargs (keyword arguments) to change the orders
```python
name = "animesh"
age = 41
# Kwargs
message_3 = "Hello {name} ({age})".format(name=name, age=age)
```


## Formatted String Literals ##

* We have a very simple usecase for using formatted string literals
```python
name = "animesh"
age = 41
message = f"Hello {name} ({age})"
```