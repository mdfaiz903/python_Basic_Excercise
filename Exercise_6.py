#check whether given number is even or odd
o_flag = 0
e_flag = 0
for i in range(0,101):
    if i%2==0:
        print(f"{i} is Even number")
        e_flag+=1
    elif i%2==1:
        print(f"{i} is Odd number")
        o_flag+=1
    else:
        print(f"{i} is Zero")

print(e_flag)
print(o_flag)

   