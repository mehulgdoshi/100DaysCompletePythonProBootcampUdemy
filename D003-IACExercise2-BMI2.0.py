# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi = int(round(weight / (height ** 2), 0))
interpretation_msg = ""
if bmi < 18.5:
    interpretation_msg = "are underweight"
elif bmi < 25:
    interpretation_msg = "have a normal weight"
elif bmi < 30:
    interpretation_msg = "are overweight"
elif bmi < 35:
    interpretation_msg = "are obese"
else:
    interpretation_msg = "are clinically obese"

print(f"Your BMI is {bmi}, you {interpretation_msg}.")




