# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
height_convert = float(height)
weight_convert = int(weight)

height_calculation = (weight_convert) / (height_convert * height_convert)

height_calculator = round(height_calculation)   


if height_calculator < 18.5 :
    print(f"Your BMI is {height_calculator}, you are underweight.")
elif height_calculator < 25 :
    print(f"Your BMI is {height_calculator}, you have a normal weight.")
elif height_calculator < 30 :
    print(f"Your BMI is {height_calculator}, you are slightly overweight.")
elif height_calculator < 35 :
    print(f"Your BMI is {height_calculator}, you are obese.")
else :
    print(f"Your BMI is{height_calculator}, you are clinically obese")