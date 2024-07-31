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

# Write your twice_as_large function here:
def twice_as_large(num1, num2):
  if num1 > num2*2:
    return True


  # Write your divisible_by_ten() function here:
def divisible_by_ten(num):
  if (num % 10 == 0):
    return True
  else:
    return False
result = divisible_by_ten(10)
print(result)

# Uncomment these print() function calls to test your divisible_by_ten() function:

#print(divisible_by_ten(20))
# should print True
#print(divisible_by_ten(25))
# should print False
  else:
    return False
result = twice_as_large (100,25)
print(result)

# Write your same_name function here:
def same_name(your_name, my_name):
  if your_name == my_name:
    return True
  else:
   return False
result = same_name("Colby", "Colby")
print(result)

result = same_name("Tina", "Amber")
print(result)

# Uncomment these function calls to test your same_name function:
#print(same_name("Colby", "Colby"))
# should print True
#print(same_name("Tina", "Amber"))
# should print False


# Write your max_num function here:
def max_num(num1, num2, num3):
  if num1>num2 and num1>num3:
   return num1
  elif num2>num1 and num2>num3:
    return num2
  elif num3>num1 and num3>num2:
    return num3
  else:
    return "It's a tie!"
# Uncomment these function calls to test your max_num function:
#print(max_num(-10, 0, 10))
print(max_num(-10, 0, 10))
# should print 10
#print(max_num(-10, 5, -30))
print(max_num(-10, 5, -30))
# should print 5
#print(max_num(-5, -10, -10))
print(max_num(-5, -10, -10))
# should print -5
#print(max_num(2, 3, 3))
print(max_num(2, 3, 3))
# should print "It's a tie!"


# Write your movie_review function here:
def movie_review(rating):
  if (rating <= 5):
    return "Avoid at all costs!"
  if (rating <9):
    return "This one was fun"
  return "Outstanding"



# Uncomment these function calls to test your movie_review function:
#print(movie_review(9))
print(movie_review(9))
# should print "Outstanding!"
#print(movie_review(4))
print(movie_review(4))
# should print "Avoid at all costs!"
#print(movie_review(6))
print(movie_review(6))
# should print "This one was fun."

#Write your function here
def append_size(my_list):
  my_list.append(len(my_list))
  return my_list



#Uncomment the line below when your function is done
append_size([23, 42, 108])

#print(append_size([23, 42, 108]))
print(append_size([23, 42 , 108]))

