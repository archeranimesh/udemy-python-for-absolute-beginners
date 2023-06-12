# Section 06 | Control Flow #

## Overview of Control Flow ##

* It helps to identify which code will execute.
* Python execute the code sequentially.
* We can write custom logic based on conditions.
    * we can use `if` statement.

```python
name = "animesh"
age = 16
if age == 16 :
    message = f"Hello {name} ({age}) - You are 16!"
else:
    message = f"Hello {name} ({age})"
print(message)

```

## Introduction to Conditions ##

* Statement which are evaluated to either `True` or `False`.
* Generally use with control flow statement.
    * `if`
    * `while`
* Operators
    * equals : `==` check for equality.
    * not equals : `!=` not equals.
    * less than : `<`
    * greater than : `>`
    * less than equal to : `<=`
    * greater than equal to : `>=`

## Practice ##
### If statements ###

* `else` statement can be used along with the `if` statements.
    * if the first block is not executed then the `else` block is executed.
* `elif`: use as else if
* there can be multiple `elif` statement in the `if` statement, but only one `if` and `else` statement.
* `elif` and `else` statement are optional.

### if, and, or statement ###

* Add extra complexity to the `if` statements.
* `and` is used when we need to check both condition should be satisfied to execute the code.
    * `if age >= 17 and location == "UK":`
        * In the above `if` condition, if `age` is greater than or equal to `17` along with `location` being `UK`, the if statement will be excuted.
        
* `or` is used when we need to check any one condition should be enough to execute.
    * `if age >= 17 or location == "UK":`
        * if the `age` is greater than `17`, or the `location` is `UK`, it will excute the if statement.
        * if the `age` is `>=` `17` it will not check the `location` condition.


### nested if ###

* We can have one `if` inside another `if`

```python
age = 17
passed_driving_test = True

if age >= 17:
    if passed_driving_test is True:
        print("You are allowed to drive.")
    else:
        print("You can learn to drive.")
else:
    print("You are not old enough to drive.")

```
* In the above code, we see the `age` is `17`, so the first part of the `if` will be executing.
* `passed_driving_test` variable is `True` , we can use the `is` or `==` will be used interchangebly.

### for loops ###

* `for` loops are used for iteration, i.e. doing something multiple times.
* The basic syntax of `for` loop is

```python
name = "animesh"

for character in name:
    print(character)
```
* We supply a array of character in the variable `name`, and the `for` loop pick individual character and prints them.

* We can also use the `for` loop over a range of number using the `range` function

```python
for x in range(0, 10):
    print(x)
```
* The `for` loop prints from 0 to 9, as the `range` function includes the first parameter and goes till 2nd arguments - 1 value. 

### while loops ###

* `while` loops is used to execute a code till the loop variable is `True`.
* Basic `while` loops looks like this

```python
x = 1

while x < 10:
    print(x)
    x += 1
```
* In the above example, the loop will execute till the value of `x` does not become `10` or more than `10`.
* The increment is done by `x += 1` line.

* `continue`, we can use this keyword to restart the loop.

```python
x = 1

while x < 10:
    if x == 4:
        x += 1
        continue

    print(x)
    x += 1
```
* in the above example, when the value of `x` it will increment the value of `x` and restart the loop at `5`.
* it will not print anything after the `continue` statements.

* `break` is used to exit from the loop on matching some conditions.

```python
x = 1
while x < 10:
    if x == 4:
        break

    print(x)
    x += 1
```
* when the value of `x` is `4` it will break the loop.