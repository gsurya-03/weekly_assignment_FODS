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

def divison_num(a,b):
    if a>b:
        div = a/b
    elif b>a:
        div = b/a
    return divison_num

def floor_div(a,b):
    f_div = a//b
    return f_div

def expo_num(a,b):
    opt = int(input("How you want to align {a}^{b} or {b}^{a}:\nFor {a}^{b} Press 1\nFor {b}^{a} Press 2\nChoose: "))
    if opt == 1:
        expo = a**b
    elif opt == 2:
        expo = b**a
    return expo

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: ")) 

print("The sum of 2 numbers are ", add_num(num1, num2))
print("The difference of 2 numbers are ",diff_num(num1, num2))
print("The product of 2 numbers are ", product_num(num1, num2))
print("The divison of 2 numbers are ", divison_num(num1, num2))
print("The floor divison of 2 numbers are ", floor_div(num1, num2))
print("The exponentiation of 2 numbers are ", expo_num(num1 , num2))
