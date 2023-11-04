#write a program to find how many days,week,month we have left.If we live until 90 year old

c_y = int(input("Enter your current age: "))

remain_year = 90-c_y



print(f"you have {remain_year*365}days, {remain_year*52}weeks, {remain_year*12}month left")