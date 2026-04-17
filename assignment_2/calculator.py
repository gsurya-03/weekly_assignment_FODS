def add_num(a,b):
    sum = a+b
    return sum

def diff_num(a,b):
    if a>b:
        diff = a-b
    elif a<b:
        diff = b-a
    return diff

def product_num(a,b):
    pro = a*b
    return pro

def quotient_num(a,b):
    if a>b and b != 0:
        quot = a/b
        return quot
    elif a<b and a != 0:
        quot = b/a
        return quot

num1 = 4
num2 = 2

print("The sum of 2 number is ", add_num(num1,num2))
print("The difference of 2 number is ",diff_num(num1, num2))
print("The product of 2 number is ", product_num(num1, num2))
print("The quotient of 2 number is ", quotient_num(num1, num2))
