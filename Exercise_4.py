a=5
print(id(a))
a=8
print(id(a))

#wirte a program for finding BMI using weight & height

w = float(input("Enter you Weight (kg): "))
h = float(input("Enter you height (m): "))

BMI = w//(h*h)
print("Your BMI: ",BMI)