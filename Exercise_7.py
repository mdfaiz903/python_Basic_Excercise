weight = int(input("Enter your weight in (KG) : "))
height = float(input("Enter your weight in (metter) : "))
BMI = weight//(height*height)
print(f"Your BMI is: {BMI}")
if (BMI<16):
    print(f"Your BMI is: {BMI} and you are Underweight (Severe thinness)")
elif( BMI>16 and BMI<16.9):
       print(f"Your BMI is: {BMI} and you are Underweight (Moderate thinness)")
elif( BMI>17 and BMI<18.4):
       print(f"Your BMI is: {BMI} and you are Underweight (Mild thinness)")

elif( BMI>18.5 and BMI<24.9):
       print(f"Your BMI is: {BMI} and you are Normal range	")

elif( BMI>25 and BMI<29.9):
       print(f"Your BMI is: {BMI} and you are Overweight (Pre-obese)")

elif( BMI>30 and BMI<34.9):
       print(f"Your BMI is: {BMI} and you are Obese (Class I)")

elif( BMI>35 and BMI<39.9):
       print(f"Your BMI is: {BMI} and you are Obese (Class II)")

elif(BMI>=40):
       print(f"Your BMI is: {BMI} and you areObese (Class III)")  