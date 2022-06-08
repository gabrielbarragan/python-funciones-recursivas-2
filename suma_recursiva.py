"""Recursive function"""

def mysum(numbers):
    """recursive function to add numbers of list"""
    sum_1= 0
    for number in numbers:
        # when number is a list
        if type(number) == list:
            sum_1+= mysum(number)
        # when number is not a list
        else:
            sum_1 += number
    
    return sum_1

if __name__ == '__main__':
    
    """driver code"""

    print(mysum([10,[21,32,43],54,[63,[72,81],90]]) == 466)
    print(mysum([10,[21,[32,43]],[54,[63,[72,81]],90]]) == 466)
    print(mysum([10,[21,[32,43]],54,[63,[72,81,[1,1,[1,1]]],90]]) == 470)