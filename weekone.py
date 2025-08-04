# We are going to Create a simple Python program that asks the user to input two numbers and a mathematical operation (addition, subtraction, multiplication, or division).

# Step 1: Ask the user to input the first number
num1= float(input("Enter the first number: "))

#step 2: Ask the user to input the second number
num2= float(input("Enter the second number: "))

# Step 3: Perform all four Operations1 
operation = input("Enter +, -, *, or /:")

# step 4: Let's do some calculations
#Add the two numbers
sum_result = num1 + num2 

#Subtract the second number from the first number
difference_result = num1 - num2 

#Multiply the two numbers
product_result = num1 * num2

#Divide the first number by the Second number
quotient_result = num1 / num2

#Step 5: Show the user what we got after calculations
print(f"Results of your two numbers:")
print(f"Sum: {sum_result}")
print(f"Difference: {difference_result}") 
print(f"Product: {product_result}")
print(f"Quotient: {quotient_result}")