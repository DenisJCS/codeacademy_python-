num1 = 6
num2 = 3

# Write your if statement here
if num1+num2 !=10:
  not_ten = True
else:
  not_ten = False

# Uncomment the below lines to show the result
# print("Does the sum of the numbers equal 10? " + str(not_ten))

# Monthly budget
budget = 2000

# Monthly expenses
food_bill = 200
electricity_bill = 100
internet_bill = 60
rent = 1500

# Calculate the total amount of expenses
total = food_bill + electricity_bill + internet_bill + rent
print(total)
# Check if the total is greater than the budget and store the result in over_budget
if total > budget :
  over_budget = True
else:
  over_budget = False

# Uncomment the below lines to see the results
print(over_budget)
print("\nTotal : " + str(total))


# Write your large_power function here:
def large_power (base , exponent):
  """Check weather if it over 5000"""
  if base ** exponent > 5000:
    return True
  else:
    return False

result = large_power(5000, 1)
print(result)
