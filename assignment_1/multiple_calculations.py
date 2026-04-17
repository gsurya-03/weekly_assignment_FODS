# Variable declearation part 
a = int(input("Enter a number: ")) # The user enters the number 
print(f"The cube of {a} is ", a**3)
print(f"The cube root of {a} is ", round(a ** (1/3), 10))
print(f"The {a} raised to the power of six is", a**6)

# For Natural logarithm
# ln(x) = 2 * [(x-1)/(x+1) + (1/3)*((x-1)/(x+1))^3 + (1/5)*((x-1)/(x+1))^5]
x = (a - 1) / (a + 1)
ln = 2 * (x + (x**3)/3 + (x**5)/5)
print(f"The natural logarithm of {a} is ", ln)

# For Base-2 logarithm
# log2(a) = ln(a) / ln(2)
x2 = (2 - 1) / (2 + 1)
ln2 = 2 * (x2 + (x2**3)/3 + (x2**5)/5)
log2 = ln / ln2
print(f"The Base-2 logarithm of {a} is", log2)