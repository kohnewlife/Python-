# This program is excuted to compute body mass index as known as BMI
# Get the weight in pounds from the user
weight = int(input("Please enter your weight in pounds: "))
print("Next, enter your height in feet and inches . . .")
# Get the height in feet and inches from the user
feet = int(input("Enter feet: "))
inches = int(input("Enter inches: "))
# Perform the conversions
# First, convert weight in pounds to weight in kilograms
# Let's call it mass in kilograms
mass = weight*0.454    # 1 pound = 0.454 kilograms
# Second, convert height in feet and inches to height in meters
# Get the total inches
total_inches = inches + feet*12    # 12 inches = 1 foot
height = total_inches*0.0254    # 1 inch = 0.0254 meters
# Compute the BMI
BMI = mass/(height*height) 
print()
# Classify the BMI number
# Create an empty classification to build upon
classification = ''
if BMI < 18.5:
    classification = "UNDERWEIGHT" # 
elif 18.5 <= BMI < 25:
    classification = "NORMAL WEIGHT"
elif 25 <= BMI < 30:
    classification = "OVERWEIGHT"
elif BMI >= 30:
    classification = "OBESE"
print("Your BMI is", BMI)
print("Your classification is", classification)
    
    
    