# Program to swap two numbers without using the third variable
# STEP 1: START.
# STEP 2: ENTER x, y.
# STEP 3: PRINT x, y.
# STEP 4: x = x + y.
# STEP 5: y= x - y.
# STEP 6: x =x - y.
# STEP 7: PRINT x, y.
# STEP 8: END.

a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))
# now a is =15
a = a+b
# now b is = 5
b=a-b
#now a become swaping
a=a-b
print("After swaping: ",a,b)

# print(swap(a,b))
# def swap(a,b):

#     temp = a
#     a=b
#     b=temp
#     return a,b



