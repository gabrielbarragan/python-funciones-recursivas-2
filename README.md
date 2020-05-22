# Recursive Function Problem

Company `RecursivX, S.A.P.I. de C.V.` has the following problem:

```python
def sum(numbers):
    """function to sum numbers of list"""
	sum_1 = 0 
	for number in numbers:
	    sum_1 += x

    return sum_1

print(sum([10,[21,32,43],54,[63,[72,81],90]]))    
```
```
Traceback (most recent call last):
  File "max.py", line 109, in <module>
    print(sum([10,[21,32,43],54,[63,[72,81],90]])) 
  File "max.py", line 105, in sum
    sum_1 += number
TypeError: unsupported operand type(s) for +=: 'int' and 'list'
```

> You get an error because when you try to add the second item, python is unable to add an int and a list; the two are separate data types. 

 

Define a recursive function that solves this particular problem:

```python
"""Recursive function"""

def sum(numbers):
    """recursive function to sum numbers of list"""
    
    # print("input numbers: ")

    # when not numbers
    

    # when index '0' of numbers is a list
    
   
    # when index '0' of numbers is not a list


``` 

```python
"""driver code"""

print(mysum([10,[21,32,43],54,[63,[72,81],90]]) == 466)
print(mysum([10,[21,[32,43]],[54,[63,[72,81]],90]]) == 466)
print(mysum([10,[21,[32,43]],54,[63,[72,81,[1,1,[1,1]]],90]]) == 470)

```

To better understand this, CTO has added a couple of tests of print statements to our function.

```
input numbers: [10, [21, 32, 43], 54]
else  numbers: [10, [21, 32, 43], 54] numbers[0] 10 numbers[1:] [[21, 32, 43], 54]
input numbers: [[21, 32, 43], 54]
numbers[0] is list
input numbers: [21, 32, 43]
else  numbers: [21, 32, 43] numbers[0] 21 numbers[1:] [32, 43]
input numbers: [32, 43]
else  numbers: [32, 43] numbers[0] 32 numbers[1:] [43]
input numbers: [43]
else  numbers: [43] numbers[0] 43 numbers[1:] []
input numbers: []
not   numbers: []
input numbers: [54]
else  numbers: [54] numbers[0] 54 numbers[1:] []
input numbers: []
not   numbers: []


160
``` 